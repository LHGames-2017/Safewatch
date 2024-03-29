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

    mapArr = []
    for x in range(0,len(deserialized_map)):
        sys.stdout.write(str(x) + "|")
        row = []
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

    tilesWithContent = []
    for tile in deserialized_map[0]:
        if tile.Content == TileContent.Resource:
            tilesWithContent.append(tile)
    print('Position:')
    print(Point(pos['X'], pos['Y']))
    playerPoint = Point(pos['X'], pos['Y'])
    return gatherResources(player, playerPoint, deserialized_map)
def goTo(start, goal, map):
    frontiers = Queue()
    pStart = (start.X, start.Y)
    pGoal = (goal.X, goal.Y)
    frontiers.put(pStart)
    cameFrom = {}
    cameFrom[pStart] = None
    print('start: (%d, %d)  goal: (%d, %d)' % (start.X, start.Y, goal.X, goal.Y))

    while not frontiers.empty():
        current = frontiers.get()
        #print('currentX:%d, currentY:%d' %(current.X, current.Y))
        for next in neighbours(current, map):
            print('next : (%d, %d)' % (next[0], next[1]))
            if next not in cameFrom:
                cameFrom[next] = current
                frontiers.put(next)
            if (next[0] == pGoal[0]) and (next[1] == pGoal[1]):
                print('found')
                break
    pathMoves = []

    if pGoal in cameFrom:
        current = pGoal
        while cameFrom[current] is not None:
            #removed since we return absolute position
            # pathMoves.append(getMove(cameFrom[current], current))
            pathMoves.append(cameFrom[current])
            current = cameFrom[current]
        print('move:', pathMoves[-2])
        return create_move_action(Point(pathMoves[-2][0], pathMoves[-2][1]))
    else:
        print('wth')
        return None

def getMove(origin, goal):
    return Point(goal.X - origin.X, goal.Y - origin.Y)

#For GoTo local search
def neighbours(pos, map):
    neighbours = []
    x = pos[0]
    y = pos[1]
    for tiles in map:
        for tile in tiles:
            if (tile.Content != TileContent.Lava and tile.Content != TileContent.Player):
                if tile.X == x - 1 and tile.Y == y:
                    neighbours.append((tile.X, tile.Y))
                if tile.X == x + 1 and tile.Y == y:
                    neighbours.append((tile.X, tile.Y))
                if tile.X == x and tile.Y - 1 == y:
                    neighbours.append((tile.X, tile.Y))
                if tile.X == x and tile.Y + 1 == y:
                    neighbours.append((tile.X, tile.Y))
    return neighbours



def printTiles(tiles):
    for tile in tiles:
        print('Content :%s PosX:%d PosY:%d' % (tile.Content, tile.X, tile.Y))

def printTilesWithDistance(tiles, playerPos):
    for tile in tiles:
        print('Content :%s PosX:%d PosY:%d Distance:%d' % (tile.Content, tile.X, tile.Y, Point(tile.X, tile.Y).Distance(playerPos, Point(tile.X, tile.Y))))

def gatherResources(player, playerPosition, tiles):
    return checkNearestTiles(playerPosition, tiles)
    #if player.CarriedRessources >= 1000:
    #    return goTo(playerPosition, player.HouseLocation, tiles)
    #else:
    #    return checkNearestTiles(playerPosition, tiles)
def checkNearestTiles(player, map):
    #print('first (%d, %d)' % (tiles[0].X, tiles[0].Y))
    tiles = []
    for tileRows in map:
        for tile in tileRows:
            if tile.Content == TileContent.Resource:
                tiles.append(tile)
    tiles.sort(key=lambda t: player.Distance(player, Point(t.X, t.Y)), reverse=False)
    closestResource = Point(tiles[0].X, tiles[0].Y)
    #On check si il est à un de distance:
    if isCloseByOne(player, closestResource):
        return create_collect_action(closestResource)
    else:
        return goTo(player, closestResource, map)

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