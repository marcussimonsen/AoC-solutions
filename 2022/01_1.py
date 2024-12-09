import sys

highest = 0
current = 0

lines = sys.stdin.readlines()

for line in lines:
    if line ==  "\n":
        highest = max(current, highest)
        current = 0
    else:
        current += int(line)

print(highest)