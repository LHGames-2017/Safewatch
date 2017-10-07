from flask import Flask, request
from structs import *
from queue import *
import json
import sys
import numpy

app = Flask(__name__)

def create_action(action_type, target):
    actionContent = ActionContent(action_type, target.__dict__)
    return json.dumps(actionContent.__dict__)

def create_move_action(target):
    return create_action("MoveAction", target)

def create_attack_action(target):
    return create_action("AttackAction", target)

def create_collect_action(target):
    return create_action("CollectAction", target)

def create_steal_action(target):
    return create_action("StealAction", target)

def create_heal_action():
    return create_action("HealAction", "")

def create_purchase_action(item):
    return create_action("PurchaseAction", item)

def deserialize_map(serialized_map):
    """
    Fonction utilitaire pour comprendre la map
    """
    serialized_map = serialized_map[1:]
    rows = serialized_map.split('[')
    column = rows[0].split('{')
    deserialized_map = [[Tile() for x in range(20)] for y in range(20)]
    for i in range(len(rows) - 1):
        column = rows[i + 1].split('{')

        for j in range(len(column) - 1):
            infos = column[j + 1].split(',')
            end_index = infos[2].find('}')
            content = int(infos[0])
            x = int(infos[1])
            y = int(infos[2][:end_index])
            deserialized_map[i][j] = Tile(content, x, y)

    return deserialized_map

def bot():
    """
    Main de votre bot.
    """
    map_json = request.form["map"]

    # Player info

    encoded_map = map_json.encode()
    map_json = json.loads(encoded_map.decode("utf-8"))
    p = map_json["Player"]
    pos = p["Position"]
    x = pos["X"]
    y = pos["Y"]
    house = p["HouseLocation"]
    player = Player(p["Health"], p["MaxHealth"], Point(x,y),
                    Point(house["X"], house["Y"]),
                    p["CarriedResources"], p["CarryingCapacity"])

    # Map
    serialized_map = map_json["CustomSerializedMap"]
    deserialized_map = deserialize_map(serialized_map)

    for x in range(0,len(deserialized_map)):
        sys.stdout.write(str(x) + "|")
        for y in range(0, len(deserialized_map[x])):
            if deserialized_map[x][y].Content == 0:
                sys.stdout.write("█")
            if deserialized_map[x][y].Content == 1:
                sys.stdout.write("A")
            if deserialized_map[x][y].Content == 2:
                sys.stdout.write("B")
            if deserialized_map[x][y].Content == 3:
                sys.stdout.write("B")
        sys.stdout.write("\n")

    otherPlayers = []

    def Map(x, y):
        return deserialized_map[x][y].Content

    print(Map(6,0))

    for player_dict in map_json["OtherPlayers"]:
        for player_name in player_dict.keys():
            player_info = player_dict[player_name]
            print(player_info)
            p_pos = player_info["Position"]
            player_info = PlayerInfo(player_info["Health"],
                                     player_info["MaxHealth"],
                                     Point(p_pos["X"], p_pos["Y"]))

            otherPlayers.append({player_name: player_info })

    # return decision
    return create_move_action(Point(0,1))
def goTo(start, goal, map):
    print(map)
    frontiers = Queue()
    frontiers.put(start)

    cameFrom = {}
    cameFrom[start] = None

    while not frontiers.empty():
        current = frontiers.get()
        for next in neighbors(current, map):
            if next not in cameFrom:
                cameFrom[next] = current
            if next == goal:
                break
    pathMoves = []
    if goal in cameFrom:
        current = goal
        while cameFrom[current] is not None:
            pathMoves.append(getMove(cameFrom[current], current))
            current = cameFrom[current]
        pathMoves.reverse()
        return pathMoves[0]
    else:
        return None

def getMove(origin, goal):
    return Point(goal.X - origin.X, goal.Y - origin.Y)

#For GoTo local search
def neighbors(pos, grid):
    result = []
    rangex = len(grid)
    rangey = (len(grid[0]))
    if 0 <= pos.Y - 1 < rangey and grid[pos.X][pos.Y - 1] == 1:
        result.append((pos.X, pos.Y - 1))
    if 0 <= pos.Y + 1 < rangey and grid[pos.X][pos.Y + 1] == 1:
        result.append((pos.X, pos.Y + 1))
    if 0 <= pos.X + 1 < rangex and grid[pos.X + 1][pos.Y] == 1:
        result.append((pos.X + 1, pos.Y))
    return result



def printTiles(tiles):
    for tile in tiles:
        print('Content :%s PosX:%d PosY:%d' % (tile.Content, tile.X, tile.Y))

def printTilesWithDistance(tiles, playerPos):
    for tile in tiles:
        print('Content :%s PosX:%d PosY:%d Distance:%d' % (tile.Content, tile.X, tile.Y, Point(tile.X, tile.Y).Distance(playerPos, Point(tile.X, tile.Y))))

def checkNearestTiles(player, tiles):
    #print('first (%d, %d)' % (tiles[0].X, tiles[0].Y))
    tiles.sort(key=lambda t: player.Distance(player, Point(t.X, t.Y)), reverse=False)
    closestResource = tiles[0]
    #On check si il est à un de distance:
    if isCloseByOne(player, closestResource):
        return create_collect_action(closestResource)
    else:
        return goTo(player, closestResource)

def isCloseByOne(player, tile):
    return (abs(player.X - tile.X) + abs(player.Y - tile.Y)) == 1

@app.route("/", methods=["POST"])
def reponse():
    # print(request.form)
    """
    Point d'entree appelle par le GameServer
    """
    return bot()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)