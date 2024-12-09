import sys

def idxToStack(i):
    return int((i - 1) / 4)

def reverse(stack):
    tmp = []
    while len(stack) > 0:
        tmp.append(stack.pop())
    return tmp

lines = sys.stdin.readlines()

i = 0

stacks = []
stacks.append([])

# Read stacks
while True:
    line = lines[i]
    if line == "\n":
        break
    
    # Add crates
    idx = 1
    # For each crate in line
    while idx < len(line):
        if line[idx] == ' ':
            idx += 4
            continue
        elif ord(line[idx]) < 64:
            break
        # Add stacks if needed
        while len(stacks) < idxToStack(idx)+1:
            stacks.append([])
        stacks[idxToStack(idx)].append(line[idx])
        idx += 4
    i += 1
i += 1
# Reverse stacks
for j in range(len(stacks)):
    stacks[j] = reverse(stacks[j])

# Perform operations
while i < len(lines):
    words = lines[i].split(' ')
    n = int(words[1])
    a = int(words[3])-1
    b = int(words[5])-1

    for j in range(n):
        stacks[b].append(stacks[a].pop())
    i += 1

# Print results
result = ""
for stack in stacks:
    result += stack.pop()
print(result)