import sys

def cycleActivate(cycle):
    return (cycle + 20) % 40 == 0

lines = sys.stdin.readlines()

i = 0

cycle = 0
register = 1
signalStrengths = []

while i < len(lines):
    line = lines[i].strip()
    if line == "noop":
        cycle += 1
        if cycleActivate(cycle):
            signalStrengths.append(cycle * register)
    else:
        command, amount = line.split(' ')
        amount = int(amount)
        cycle += 1
        if cycleActivate(cycle):
            signalStrengths.append(cycle * register)
        cycle += 1
        if cycleActivate(cycle):
            signalStrengths.append(cycle * register)
        register += amount
    i += 1

print(sum(signalStrengths))