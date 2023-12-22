#!/usr/bin/python3
import sys

WHITE = '\033[0m'
GREEN = '\033[92m'

def start(lines, x, y):
    while x > 0 and lines[y][x - 1].isdecimal():
        x -= 1
    return x, y

def getNum(lines, x, y):
    num = ""
    while x < len(lines[y]) and lines[y][x].isdecimal():
        num += lines[y][x]
        x += 1
    return int(num)

def main():
    lines = sys.stdin.readlines()
    nums = []
    for y in range(len(lines)):
        for x, c in enumerate(lines[y].strip()):
            if c == '.' or c.isdecimal():
                continue
            for dy in range(-1, 2):
                if y + dy < 0 or y + dy >= len(lines):
                    continue
                for dx in range(-1, 2):
                    if x + dx < 0 or x + dx >= len(lines[y + dy]):
                        continue
                    if dx == 0 and dy == 0:
                        continue
                    if not lines[y + dy][x + dx].isdecimal():
                        continue
                    n = start(lines, x + dx, y + dy)

                    if n not in nums:
                        nums.append(n)

    # Testing
    '''
    for y in range(len(lines)):
        x = 0
        while x < len(lines[y]):
            if (x, y) in nums:
                while x < len(lines[y]) and lines[y][x].isdecimal():
                    print(GREEN + lines[y][x], end='')
                    x += 1
            else:
                print(WHITE + lines[y][x], end='')
                x += 1
    '''

    total = 0
    for x, y in nums:
        total += getNum(lines, x, y)
    print(total)

if __name__ == '__main__':
    main()
