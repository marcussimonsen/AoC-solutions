import sys

handDict = {
    'X': 1,
    'Y': 2,
    'Z': 3,
    'A': 1,
    'B': 2,
    'C': 3
}

pairDict = {
    (1, 1): 3,
    (1, 2): 6,
    (1, 3): 0,
    (2, 1): 0,
    (2, 2): 3,
    (2, 3): 6,
    (3, 1): 6,
    (3, 2): 0,
    (3, 3): 3,
}

def points(a, b):
    val1 = handDict[a]
    val2 = handDict[b]

    return pairDict[val1, val2]

lines = sys.stdin.readlines()

total = 0

for line in lines:
    total += handDict[line[2]]
    total += points(line[0], line[2])

print(total)
