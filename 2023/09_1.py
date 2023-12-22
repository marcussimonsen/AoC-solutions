#!/usr/bin/python3

import sys

def find_next(nums):
    lines = [nums]
    last_line = nums
    while sum(last_line) != 0:
        new_line = []
        for i, j in zip(last_line, last_line[1:]):
            new_line.append(j - i)
        lines.append(new_line)
        last_line = new_line
    for i in reversed(range(len(lines))):
        if i == 0:
            continue
        lines[i-1].append(lines[i-1][len(lines[i-1])-1] + lines[i][len(lines[i])-1])
    return lines[0][len(lines[0])-1]


def main():
    lines = sys.stdin.readlines()

    res = 0
    for line in lines:
        res += find_next([int(num) for num in line.split()])
    print(res)

if __name__ == "__main__":
    main()
