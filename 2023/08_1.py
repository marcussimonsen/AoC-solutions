#!/usr/bin/python3
import sys
import re

class Option:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

    def __repr__(self):
        return self.name

def main():
    lines = sys.stdin.readlines()
    
    instructions = lines[0].strip()

    graph = {}

    pattern = r"(.{3}) = \((.{3}), (.{3})\)"

    for line in lines[2:]:
        m = re.match(pattern, line)
        name, left, right = m.groups()
        graph[name] = Option(name, left, right)

    current = graph["AAA"]
    steps = 0
    while current.name != "ZZZ":
        if instructions[steps % len(instructions)] == "L":
            current = graph[current.left]
        else:
            current = graph[current.right]
        steps += 1
    
    print(steps)

if __name__ == "__main__":
    main()
