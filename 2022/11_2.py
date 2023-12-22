import sys
import time

class Monkey:
    def __init__(self):
        self.items = []
        self.itemsInspected = 0
        self.operator = ''
        self.operatorFactor = 0
        self.divisible = 0
        self.ifTrue = 0
        self.ifFalse = 0
    
    def getOperatorFactor(self, item):
        return self.operatorFactor if self.operatorFactor != 'old' else item
    
    def getThrowTo(self, item):
        if item % self.divisible == 0:
            return self.ifTrue
        else:
            return self.ifFalse
    
    def print(self):
        print("____ Monkey ____")
        print(self.items)
        print(self.operator)
        print(self.operatorFactor)
        print(self.divisible)
        print(self.ifTrue)
        print(self.ifFalse)
        print(self.itemsInspected)

lines = sys.stdin.readlines()

monkeys = []

# Reading input
i = 0
while i < len(lines):
    monkey = Monkey()

    # items
    items = lines[i+1][18:].strip().split(', ')
    items = [int(item) for item in items]
    # operator
    operator = lines[i+2][23]
    operatorFactor = lines[i+2][25:].strip()
    try:
        operatorFactor = int(operatorFactor)
    except:
        operatorFactor = operatorFactor
    # divisible
    divisible = int(lines[i+3][21:].strip())
    # ifTrue & ifFalse
    ifTrue = int(lines[i+4][28:].strip())
    ifFalse = int(lines[i+5][29:].strip())

    monkey.items = items
    monkey.operator = operator
    monkey.operatorFactor = operatorFactor
    monkey.divisible = divisible
    monkey.ifTrue = ifTrue
    monkey.ifFalse = ifFalse

    monkeys.append(monkey)
    i += 7

timeStamp = time.time()
print("timeStamp: " + str(timeStamp))

rounds = 10_000
# Rounds
while rounds > 0:
    i = 0
    if rounds != 10_000 and (rounds == 9_999 or rounds == 9_980 or rounds % 1000 == 0):
        print("After round " + str(10_000 - rounds))
        for j in range(len(monkeys)):
            print("Monkey " + str(j) + " inspected items " + str(monkeys[j].itemsInspected) + " times.")
    if time.time() - timeStamp >= 5:
        print(rounds)
        timeStamp = time.time()
    for monkey in monkeys:
        while len(monkey.items) > 0:
            item = monkey.items.pop(0)
            if monkey.operator == '*':
                item = item * monkey.getOperatorFactor(item)
            elif monkey.operator == '+':
                item = item + monkey.getOperatorFactor(item)
            else:
                raise("Unknown operator exception")
            monkeys[monkey.getThrowTo(item)].items.append(item)
            monkey.itemsInspected += 1
        
        i += 1
        
    rounds -= 1

mostActive = None
secondMostActive = None

for monkey in monkeys:
    if mostActive is None or monkey.itemsInspected > mostActive.itemsInspected:
        secondMostActive = mostActive
        mostActive = monkey
    elif secondMostActive is None or monkey.itemsInspected > secondMostActive.itemsInspected:
        secondMostActive = monkey

print(mostActive.itemsInspected * secondMostActive.itemsInspected)