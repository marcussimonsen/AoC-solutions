import sys
import math

def printMap(w, h, hx, hy, tx, ty):
    map = []
    for y in range(h):
        line = []
        for x in range(w):
            line.append('H' if (x == hx and y == hy) else 'T' if (x == tx and y == ty) else '.')
        map.append(line)
    y = len(map)-1
    while y >= 0:
        line = ""
        for c in map[y]:
            line += c
        print(line)
        y -= 1

def distTo(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

lines = sys.stdin.readlines()

dirToXDict = {
    'L': -1,
    'R': 1,
    'U': 0,
    'D': 0
}
dirToYDict = {
    'L': 0,
    'R': 0,
    'U': 1,
    'D': -1
}

HX, HY = 0, 0
TX, TY = 0, 0

tailVisited = {(0, 0)}

for command in lines:
    dir, amount = command.split(' ')
    amount = int(amount)
    for i in range(amount):
        HX += dirToXDict[dir]
        HY += dirToYDict[dir]
        distToHead = distTo(TX, TY, HX, HY)
        # Move tail
        if distToHead > math.sqrt(2):
            if HX - TX != 0:
                TX += (HX - TX) / abs(HX - TX)
            if HY - TY != 0:
                TY += (HY - TY) / abs(HY - TY)
            tailVisited.add((TX, TY))

print(len(tailVisited))