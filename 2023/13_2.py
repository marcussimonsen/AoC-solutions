#!/usr/bin/python3
import sys

def horizontal_mirror(pattern):
    for i in range(len(pattern)-1):
        mistakes = 0
        for j in range(i+1):
            if i-j < 0 or i+j+1 >= len(pattern):
                break
            for k in range(len(pattern[0])):
                if pattern[i-j][k] != pattern[i+j+1][k]:
                    mistakes += 1
                    if mistakes > 1:
                        break
        if mistakes == 1:
            return i
    return -1

def vertical_mirror(pattern):
    for i in range(len(pattern[0])):
        mistakes = 0
        for j in range(i+1):
            if i-j < 0 or i+j+1 >= len(pattern[0]):
                break
            for k in range(len(pattern)):
                if pattern[k][i-j] != pattern[k][i+j+1]:
                    mistakes += 1
                    if mistakes > 1:
                        break
        if mistakes == 1:
            return i
    return -1

def main():
    lines = sys.stdin.readlines()
    i = 0
    patterns = []
    while i < len(lines):
        tmp = []
        while i < len(lines) and lines[i] != "\n":
            tmp.append(list(lines[i].strip()))
            i += 1
        patterns.append(tmp)
        i += 1

    res = 0

    for pattern in patterns:
        # Check for horizontal match
        horif = horizontal_mirror(pattern)
        if horif != -1:
            res += 100 * (horif + 1)
            continue

        # Find vertical match
        verif = vertical_mirror(pattern)
        res += verif+1

    print(res)

if __name__ == "__main__":
    main()
