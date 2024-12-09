import sys

highest = [0, 0, 0]
current = 0

lines = sys.stdin.readlines()

for line in lines:
    if line ==  "\n":
        for i in range(len(highest)):
            if current > highest[i]:
                highest[i], current = current, highest[i]
        current = 0
    else:
        current += int(line)

print("Top three highest:")
print(highest)
print("Total: " + str(sum(highest)))