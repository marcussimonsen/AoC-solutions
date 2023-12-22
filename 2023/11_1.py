#!/usr/bin/python3

import sys
from itertools import product

def main():
    image = [list(line.strip()) for line in sys.stdin]

    # Expand space horizontally
    i = 0
    while i < len(image[0]):
        if '#' not in [row[i] for row in image]:
            for row in image:
                row.insert(i, '.')
            i += 1
        i += 1

    # Expand space vertically
    i = 0
    while i < len(image):
        if '#' not in image[i]:
            image.insert(i, ['.'] * len(image[0]))
            i += 1
        i += 1

    # Locate all galaxies
    galaxies = []
    for y, row in enumerate(image):
        for x, space in enumerate(row):
            if space == '#':
                galaxies.append((x, y))

    res = 0
    for (ax, ay), (bx, by) in product(galaxies, repeat=2):
        res += abs(ax - bx) + abs(ay - by)

    print(res//2)

if __name__ == '__main__':
    main()
