import sys
map = [[{0,15,17},{0,15,18},{0,15,19},{1,15,20},{0,15,21},{0,15,22},{1,15,23},{1,15,24},{1,15,25},{1,15,26},{0,15,27},{1,15,28},{1,15,29},{1,15,30},{1,15,31},{3,15,32},{0,15,33},{0,15,34},{0,15,35},{0,15,36}],[{0,16,17},{0,16,18},{1,16,19},{0,16,20},{1,16,21},{3,16,22},{0,16,23},{0,16,24},{0,16,25},{0,16,26},{0,16,27},{0,16,28},{0,16,29},{0,16,30},{0,16,31},{1,16,32},{1,16,33},{3,16,34},{0,16,35},{0,16,36}],[{4,17,17},{0,17,18},{1,17,19},{1,17,20},{0,17,21},{0,17,22},{0,17,23},{0,17,24},{0,17,25},{0,17,26},{0,17,27},{0,17,28},{0,17,29},{0,17,30},{0,17,31},{0,17,32},{0,17,33},{1,17,34},{0,17,35},{0,17,36}],[{0,18,17},{1,18,18},{1,18,19},{0,18,20},{0,18,21},{0,18,22},{0,18,23},{0,18,24},{0,18,25},{0,18,26},{0,18,27},{0,18,28},{0,18,29},{0,18,30},{0,18,31},{0,18,32},{0,18,33},{0,18,34},{1,18,35},{0,18,36}],[{1,19,17},{1,19,18},{0,19,19},{0,19,20},{0,19,21},{0,19,22},{0,19,23},{0,19,24},{0,19,25},{0,19,26},{0,19,27},{0,19,28},{0,19,29},{0,19,30},{0,19,31},{0,19,32},{0,19,33},{0,19,34},{0,19,35},{1,19,36}],[{0,20,17},{1,20,18},{0,20,19},{0,20,20},{0,20,21},{0,20,22},{0,20,23},{0,20,24},{0,20,25},{0,20,26},{0,20,27},{0,20,28},{0,20,29},{0,20,30},{0,20,31},{0,20,32},{0,20,33},{0,20,34},{0,20,35},{1,20,36}],[{1,21,17},{0,21,18},{0,21,19},{0,21,20},{0,21,21},{0,21,22},{0,21,23},{0,21,24},{0,21,25},{0,21,26},{0,21,27},{0,21,28},{0,21,29},{0,21,30},{0,21,31},{0,21,32},{0,21,33},{0,21,34},{0,21,35},{0,21,36}],[{1,22,17},{0,22,18},{0,22,19},{0,22,20},{0,22,21},{0,22,22},{0,22,23},{0,22,24},{0,22,25},{0,22,26},{0,22,27},{0,22,28},{0,22,29},{3,22,30},{0,22,31},{0,22,32},{0,22,33},{0,22,34},{0,22,35},{0,22,36}],[{1,23,17},{0,23,18},{0,23,19},{0,23,20},{0,23,21},{0,23,22},{0,23,23},{0,23,24},{0,23,25},{0,23,26},{0,23,27},{0,23,28},{0,23,29},{0,23,30},{0,23,31},{0,23,32},{0,23,33},{0,23,34},{0,23,35},{0,23,36}],[{1,24,17},{0,24,18},{0,24,19},{0,24,20},{0,24,21},{0,24,22},{0,24,23},{0,24,24},{0,24,25},{0,24,26},{0,24,27},{0,24,28},{0,24,29},{0,24,30},{0,24,31},{0,24,32},{0,24,33},{0,24,34},{0,24,35},{0,24,36}],[{0,25,17},{0,25,18},{0,25,19},{0,25,20},{0,25,21},{0,25,22},{0,25,23},{0,25,24},{0,25,25},{0,25,26},{2,25,27},{0,25,28},{0,25,29},{0,25,30},{0,25,31},{0,25,32},{0,25,33},{0,25,34},{0,25,35},{0,25,36}],[{1,26,17},{0,26,18},{0,26,19},{0,26,20},{0,26,21},{0,26,22},{0,26,23},{0,26,24},{0,26,25},{0,26,26},{0,26,27},{0,26,28},{0,26,29},{0,26,30},{0,26,31},{0,26,32},{0,26,33},{0,26,34},{0,26,35},{0,26,36}],[{1,27,17},{0,27,18},{0,27,19},{0,27,20},{0,27,21},{0,27,22},{0,27,23},{0,27,24},{0,27,25},{0,27,26},{0,27,27},{0,27,28},{0,27,29},{0,27,30},{0,27,31},{0,27,32},{0,27,33},{0,27,34},{0,27,35},{0,27,36}],[{1,28,17},{0,28,18},{0,28,19},{0,28,20},{0,28,21},{0,28,22},{0,28,23},{0,28,24},{0,28,25},{0,28,26},{0,28,27},{0,28,28},{0,28,29},{0,28,30},{0,28,31},{0,28,32},{0,28,33},{0,28,34},{4,28,35},{0,28,36}],[{1,29,17},{0,29,18},{0,29,19},{0,29,20},{0,29,21},{0,29,22},{0,29,23},{0,29,24},{0,29,25},{0,29,26},{0,29,27},{0,29,28},{0,29,29},{0,29,30},{0,29,31},{0,29,32},{0,29,33},{0,29,34},{0,29,35},{0,29,36}],[{0,30,17},{1,30,18},{0,30,19},{0,30,20},{0,30,21},{0,30,22},{0,30,23},{0,30,24},{0,30,25},{0,30,26},{0,30,27},{0,30,28},{0,30,29},{0,30,30},{0,30,31},{0,30,32},{0,30,33},{0,30,34},{0,30,35},{1,30,36}],[{0,31,17},{1,31,18},{0,31,19},{0,31,20},{0,31,21},{0,31,22},{3,31,23},{0,31,24},{0,31,25},{0,31,26},{0,31,27},{0,31,28},{0,31,29},{0,31,30},{0,31,31},{0,31,32},{0,31,33},{0,31,34},{0,31,35},{1,31,36}],[{0,32,17},{0,32,18},{1,32,19},{0,32,20},{0,32,21},{0,32,22},{0,32,23},{0,32,24},{0,32,25},{0,32,26},{0,32,27},{0,32,28},{0,32,29},{0,32,30},{0,32,31},{0,32,32},{0,32,33},{0,32,34},{1,32,35},{0,32,36}],[{0,33,17},{0,33,18},{0,33,19},{1,33,20},{0,33,21},{0,33,22},{0,33,23},{0,33,24},{0,33,25},{0,33,26},{0,33,27},{0,33,28},{0,33,29},{0,33,30},{0,33,31},{0,33,32},{0,33,33},{1,33,34},{0,33,35},{0,33,36}],[{0,34,17},{0,34,18},{0,34,19},{0,34,20},{1,34,21},{1,34,22},{0,34,23},{0,34,24},{0,34,25},{0,34,26},{0,34,27},{0,34,28},{0,34,29},{0,34,30},{0,34,31},{1,34,32},{1,34,33},{0,34,34},{0,34,35},{0,34,36}]]
# file = [{"Player":{"Health":10,"MaxHealth":10,"CarriedResources":0,"CarryingCapacity":1000,"TotalResources":0,"AttackPower":1,"Defence":1,"Position":{"X":25,"Y":27},"HouseLocation":{"X":25,"Y":27},"Score":0,"Name":"Me"},"CustomSerializedMap":"[[{0,15,17},{0,15,18},{0,15,19},{1,15,20},{0,15,21},{0,15,22},{1,15,23},{1,15,24},{1,15,25},{1,15,26},{0,15,27},{1,15,28},{1,15,29},{1,15,30},{1,15,31},{3,15,32},{0,15,33},{0,15,34},{0,15,35},{0,15,36}],[{0,16,17},{0,16,18},{1,16,19},{0,16,20},{1,16,21},{3,16,22},{0,16,23},{0,16,24},{0,16,25},{0,16,26},{0,16,27},{0,16,28},{0,16,29},{0,16,30},{0,16,31},{1,16,32},{1,16,33},{3,16,34},{0,16,35},{0,16,36}],[{4,17,17},{0,17,18},{1,17,19},{1,17,20},{0,17,21},{0,17,22},{0,17,23},{0,17,24},{0,17,25},{0,17,26},{0,17,27},{0,17,28},{0,17,29},{0,17,30},{0,17,31},{0,17,32},{0,17,33},{1,17,34},{0,17,35},{0,17,36}],[{0,18,17},{1,18,18},{1,18,19},{0,18,20},{0,18,21},{0,18,22},{0,18,23},{0,18,24},{0,18,25},{0,18,26},{0,18,27},{0,18,28},{0,18,29},{0,18,30},{0,18,31},{0,18,32},{0,18,33},{0,18,34},{1,18,35},{0,18,36}],[{1,19,17},{1,19,18},{0,19,19},{0,19,20},{0,19,21},{0,19,22},{0,19,23},{0,19,24},{0,19,25},{0,19,26},{0,19,27},{0,19,28},{0,19,29},{0,19,30},{0,19,31},{0,19,32},{0,19,33},{0,19,34},{0,19,35},{1,19,36}],[{0,20,17},{1,20,18},{0,20,19},{0,20,20},{0,20,21},{0,20,22},{0,20,23},{0,20,24},{0,20,25},{0,20,26},{0,20,27},{0,20,28},{0,20,29},{0,20,30},{0,20,31},{0,20,32},{0,20,33},{0,20,34},{0,20,35},{1,20,36}],[{1,21,17},{0,21,18},{0,21,19},{0,21,20},{0,21,21},{0,21,22},{0,21,23},{0,21,24},{0,21,25},{0,21,26},{0,21,27},{0,21,28},{0,21,29},{0,21,30},{0,21,31},{0,21,32},{0,21,33},{0,21,34},{0,21,35},{0,21,36}],[{1,22,17},{0,22,18},{0,22,19},{0,22,20},{0,22,21},{0,22,22},{0,22,23},{0,22,24},{0,22,25},{0,22,26},{0,22,27},{0,22,28},{0,22,29},{3,22,30},{0,22,31},{0,22,32},{0,22,33},{0,22,34},{0,22,35},{0,22,36}],[{1,23,17},{0,23,18},{0,23,19},{0,23,20},{0,23,21},{0,23,22},{0,23,23},{0,23,24},{0,23,25},{0,23,26},{0,23,27},{0,23,28},{0,23,29},{0,23,30},{0,23,31},{0,23,32},{0,23,33},{0,23,34},{0,23,35},{0,23,36}],[{1,24,17},{0,24,18},{0,24,19},{0,24,20},{0,24,21},{0,24,22},{0,24,23},{0,24,24},{0,24,25},{0,24,26},{0,24,27},{0,24,28},{0,24,29},{0,24,30},{0,24,31},{0,24,32},{0,24,33},{0,24,34},{0,24,35},{0,24,36}],[{0,25,17},{0,25,18},{0,25,19},{0,25,20},{0,25,21},{0,25,22},{0,25,23},{0,25,24},{0,25,25},{0,25,26},{2,25,27},{0,25,28},{0,25,29},{0,25,30},{0,25,31},{0,25,32},{0,25,33},{0,25,34},{0,25,35},{0,25,36}],[{1,26,17},{0,26,18},{0,26,19},{0,26,20},{0,26,21},{0,26,22},{0,26,23},{0,26,24},{0,26,25},{0,26,26},{0,26,27},{0,26,28},{0,26,29},{0,26,30},{0,26,31},{0,26,32},{0,26,33},{0,26,34},{0,26,35},{0,26,36}],[{1,27,17},{0,27,18},{0,27,19},{0,27,20},{0,27,21},{0,27,22},{0,27,23},{0,27,24},{0,27,25},{0,27,26},{0,27,27},{0,27,28},{0,27,29},{0,27,30},{0,27,31},{0,27,32},{0,27,33},{0,27,34},{0,27,35},{0,27,36}],[{1,28,17},{0,28,18},{0,28,19},{0,28,20},{0,28,21},{0,28,22},{0,28,23},{0,28,24},{0,28,25},{0,28,26},{0,28,27},{0,28,28},{0,28,29},{0,28,30},{0,28,31},{0,28,32},{0,28,33},{0,28,34},{4,28,35},{0,28,36}],[{1,29,17},{0,29,18},{0,29,19},{0,29,20},{0,29,21},{0,29,22},{0,29,23},{0,29,24},{0,29,25},{0,29,26},{0,29,27},{0,29,28},{0,29,29},{0,29,30},{0,29,31},{0,29,32},{0,29,33},{0,29,34},{0,29,35},{0,29,36}],[{0,30,17},{1,30,18},{0,30,19},{0,30,20},{0,30,21},{0,30,22},{0,30,23},{0,30,24},{0,30,25},{0,30,26},{0,30,27},{0,30,28},{0,30,29},{0,30,30},{0,30,31},{0,30,32},{0,30,33},{0,30,34},{0,30,35},{1,30,36}],[{0,31,17},{1,31,18},{0,31,19},{0,31,20},{0,31,21},{0,31,22},{3,31,23},{0,31,24},{0,31,25},{0,31,26},{0,31,27},{0,31,28},{0,31,29},{0,31,30},{0,31,31},{0,31,32},{0,31,33},{0,31,34},{0,31,35},{1,31,36}],[{0,32,17},{0,32,18},{1,32,19},{0,32,20},{0,32,21},{0,32,22},{0,32,23},{0,32,24},{0,32,25},{0,32,26},{0,32,27},{0,32,28},{0,32,29},{0,32,30},{0,32,31},{0,32,32},{0,32,33},{0,32,34},{1,32,35},{0,32,36}],[{0,33,17},{0,33,18},{0,33,19},{1,33,20},{0,33,21},{0,33,22},{0,33,23},{0,33,24},{0,33,25},{0,33,26},{0,33,27},{0,33,28},{0,33,29},{0,33,30},{0,33,31},{0,33,32},{0,33,33},{1,33,34},{0,33,35},{0,33,36}],[{0,34,17},{0,34,18},{0,34,19},{0,34,20},{1,34,21},{1,34,22},{0,34,23},{0,34,24},{0,34,25},{0,34,26},{0,34,27},{0,34,28},{0,34,29},{0,34,30},{0,34,31},{1,34,32},{1,34,33},{0,34,34},{0,34,35},{0,34,36}]]","OtherPlayers":[]]
# map_json = request.form["map"]


# serialized_map = map[1:]
# rows = serialized_map.split('[')
# column = rows[0].split('{')
# deserialized_map = [[Tile() for x in range(40)] for y in range(40)]

# for tile in deserialized_map[0]:
#        print('content')
#        print(tile.Content)
#        if tile.Content != None:
#            tilesWithContent.append(tile)
for x in range(0, len(map[0])):
	sys.stdout.write(str(x))
print("")
for x in range(0,len(map)):
	for y in range(0,len(map[x])):
		if 0 in map[x][y]:
			sys.stdout.write("█")
		if 1 in map[x][y]:
			sys.stdout.write("A")
		if 2 in map[x][y]:
			sys.stdout.write("B")
		if 3 in map[x][y]:
			sys.stdout.write("C")
	sys.stdout.write("\n")