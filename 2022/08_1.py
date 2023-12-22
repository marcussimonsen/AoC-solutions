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

visibleTrees = []
for treeLine in trees:
    tmp = []
    for tree in treeLine:
        tmp.append(0)
    visibleTrees.append(tmp)

# Left to right
y = 0
while y < len(trees):
    x = 0
    currentHighest = -1
    while x < len(trees[y]):
        tree = trees[y][x]
        if tree > currentHighest:
            visibleTrees[y][x] = 1 
            currentHighest = tree
        x += 1
    y += 1

# Right to left
y = 0
while y < len(trees):
    x = len(trees[y])-1
    currentHighest = -1
    while x >= 0:
        tree = trees[y][x]
        if tree > currentHighest:
            visibleTrees[y][x] = 1 
            currentHighest = tree
        x -= 1
    y += 1

# Top to bottom
x = 0
y = 0
while x < len(trees[y]):
    currentHighest = -1
    while y < len(trees):
        tree = trees[y][x]
        if tree > currentHighest:
            visibleTrees[y][x] = 1 
            currentHighest = tree
        y += 1
    y = 0
    x += 1

# Bottom to top
x = 0
y = len(trees)-1
while x < len(trees[y]):
    currentHighest = -1
    while y >= 0:
        tree = trees[y][x]
        if tree > currentHighest:
            visibleTrees[y][x] = 1 
            currentHighest = tree
        y -= 1
    y = len(trees)-1
    x += 1

print(sum([tree for treeLine in visibleTrees for tree in treeLine]))