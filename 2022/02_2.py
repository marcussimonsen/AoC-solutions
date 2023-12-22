import sys

handDict = {
    'A': 1,
    'B': 2,
    'C': 3
}

scoreDict = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

pairDict = {
    (1, 1): 3,
    (1, 2): 0,
    (1, 3): 6,
    (2, 1): 6,
    (2, 2): 3,
    (2, 3): 0,
    (3, 1): 0,
    (3, 2): 6,
    (3, 3): 3
}

handScoreDict = {
    (1, 0): 3,
    (1, 3): 1,
    (1, 6): 2,
    (2, 0): 1,
    (2, 3): 2,
    (2, 6): 3,
    (3, 0): 2,
    (3, 3): 3,
    (3, 6): 1
}

def points(a, b):
    return pairDict[a, b]

lines = sys.stdin.readlines()

total = 0

for line in lines:
    opponentHand = handDict[line[0]]
    wantedScore = scoreDict[line[2]]

    hand = handScoreDict[opponentHand, wantedScore]

    total += hand
    total += points(hand, opponentHand)

print(total)
