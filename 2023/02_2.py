#!/usr/bin/python3
import sys
import re

def main():
    res = 0
    for line in sys.stdin:
        game, counts = line.strip().split(": ")
        counts = re.split("[,;] ", counts)
        reds = 0
        greens = 0
        blues = 0
        for count in counts:
            num, color = count.split()
            if color == "red":
                reds = max(reds, int(num))
            elif color == "green":
                greens = max(greens, int(num))
            elif color == "blue":
                blues = max(blues, int(num))
        res += reds * greens * blues

    print(res)

if __name__ == '__main__':
    main()
