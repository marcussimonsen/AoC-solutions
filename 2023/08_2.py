#!/usr/bin/python3
import sys
import re
from itertools import cycle

class Option:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

    def __repr__(self):
        return self.name

def is_solved(currents):
    for current in currents:
        if current.name[2] != 'Z':
            return False
    return True

def main():
    lines = sys.stdin.readlines()
    
    instructions = lines[0].strip()

    graph = {}

    pattern = r"(.{3}) = \((.{3}), (.{3})\)"

    currents = []

    for line in lines[2:]:
        m = re.match(pattern, line)
        name, left, right = m.groups()
        node = Option(name, left, right)
        if name.endswith('A'):
            currents.append(node)
        graph[name] = node

    steps = 0
    it = cycle(instructions)
    while True:
        for instruction in it:
            if instruction == 'L':
                currents = [graph[current.left] for current in currents]
            else:
                currents = [graph[current.right] for current in currents]
            steps += 1
            if steps % 250_000_000 == 0:
                print(steps)
            if currents[0].name[2] == 'Z':
                break
        if is_solved(currents[1:]):
            break
    
    print(steps)

if __name__ == "__main__":
    main()
