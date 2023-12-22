import sys

lines = sys.stdin.readlines()

# Grid of trees (y, x)
trees = []

for line in lines:
    line = line.strip()
    treeLine = []
    for tree in line:
        treeLine.append(int(tree))
    trees.append(treeLine)

scenicScores = []

for y in range(len(trees)):
    treeLine = []
    for x in range(len(trees[y])):
        #print(x, y)
        tree = trees[y][x]
        # Look left
        left = 0
        while x-left-1 >= 0:
            left += 1
            if trees[y][x-left] >= tree:
                break
        # Look right
        right = 0
        while x+right+1 < len(trees[y]):
            #print(x+right+1)
            right += 1
            if trees[y][x+right] >= tree:
                break
        # Look up
        up = 0
        while y-up-1 >= 0:
            up += 1
            if trees[y-up][x] >= tree:
                break
        # Look down
        down = 0
        while y+down+1 < len(trees):
            down += 1
            if trees[y+down][x] >= tree:
                break
        # Calculate score
        treeLine.append(left*right*up*down)
    scenicScores.append(treeLine)

print(max([tree for treeLine in scenicScores for tree in treeLine]))