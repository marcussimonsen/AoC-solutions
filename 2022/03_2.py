import sys

def getTriple(str1, str2, str3):
    for charA in str1:
        for charB in str2:
            for charC in str3:
                if charA == charB and charB == charC:
                    return charA

def priority(char):
    value = ord(char)
    if value > 90:
        return value-96
    else:
        return value-64+26

lines = sys.stdin.readlines()
priorities = []
group = []

for line in lines:
    group.append(line)
    if len(group) == 3:
        priorities.append(priority(getTriple(group[0], group[1], group[2])))
        group = []

print(sum(priorities))