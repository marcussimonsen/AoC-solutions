import sys

def getDouble(str1, str2):
    for charA in str1:
        for charB in str2:
            if charA == charB:
                return charA

def priority(char):
    value = ord(char)
    if value > 90:
        return value-96
    else:
        return value-64+26

lines = sys.stdin.readlines()
priorities = []

for line in lines:
    sackA = line[:int(len(line)/2)]
    sackB = line[int(len(line)/2):len(line)-1]
    
    priorities.append(priority(getDouble(sackA, sackB)))

print(sum(priorities))