import sys

class Pos:
    def __init__(self, x: int, y: int, comesFrom = None):
        self.x = x
        self.y = y
        self.comesFrom = comesFrom

    def getDistance(self):
        if self.comesFrom is None:
            return 0
        else:
            return self.comesFrom.getDistance() + 1
        #return 0 if self.comesFrom is None else self.comesFrom.getDistance() + 1

    def print(self):
        print("pos:", self.x, self.y, self.comesFrom)
    
    def __str__(self):
        return str(self.x) + " " + str(self.y)

def findPos(map, c):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == c:
                return x, y

# procedure BFS(G, root) is
#     let Q be a queue
#     label root as explored
#     Q.enqueue(root)
#     while Q is not empty do
#         v := Q.dequeue()
#         if v is the goal then
#             return v
#         for all edges from v to w in G.adjacentEdges(v) do
#             if w is not labeled as explored then
#                 label w as explored
#                 w.parent := v
#                 Q.enqueue(w)
def BFS(G, V, x, y):
    Q = []
    V[y][x] = True
    Q.append(Pos(x, y))
    while len(Q) != 0:
        v = Q.pop(0)
        if G[v.y][v.x] == 'E':
            return v
        for move in Moves:
            newX, newY = v.x + move[0], v.y + move[1]
            # Out of bounds check
            if newY < 0 or newY >= len(G) or newX < 0 or newX >= len(G[newY]):
                continue
            # Already visited check
            if V[newY][newX]:
                continue
            # Can reach check (too high)
            if (G[v.y][v.x] == 'S' and ord(G[newY][newX]) > ord('b')) or G[v.y][v.x] != 'S' and ord(G[newY][newX]) > ord(G[v.y][v.x])+1:
                continue
            # Can reach end goal check
            if G[newY][newX] == 'E' and ord(G[v.y][v.x]) < ord('y'):
                continue
            V[newY][newX] = True
            Q.append(Pos(newX, newY, v))
        

Moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

map = sys.stdin.readlines()
for i in range(len(map)):
    map[i] = map[i].strip()

startX, startY = findPos(map, 'S')

visitedMap = []
debugMap = []
for i in range(len(map)):
    tmp = []
    tmp2 = ""
    for j in range(len(map[i])):
        tmp.append(False)
        tmp2 += '.'
    visitedMap.append(tmp)
    debugMap.append(tmp2)

route = BFS(map, visitedMap, startX, startY)

# Print visited map
# for y in range(len(visitedMap)):
#     line = ""
#     for x in range(len(visitedMap[y])):
#         line += 'T' if visitedMap[y][x] else 'F'
#     print(line)

current = route
while current is not None:
    debugMap[current.y] = debugMap[current.y][:current.x] + 'X' + debugMap[current.y][current.x+1:]
    current = current.comesFrom

# Print route
for line in debugMap:
    print(line)

print(route.getDistance())