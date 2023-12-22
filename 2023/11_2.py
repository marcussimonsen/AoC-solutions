#!/usr/bin/python3

import sys

def product(galaxies):
    for i, galaxy_a in enumerate(galaxies):
        for galaxy_b in galaxies[i+1:]:
            yield galaxy_a, galaxy_b

def main():
    image = [list(line.strip()) for line in sys.stdin]

    expanding_rows = []
    expanding_cols = []

    # Expand space horizontally
    for i in range(len(image[0])):
        if '#' not in [row[i] for row in image]:
            expanding_cols.append(i)

    # Expand space vertically
    for i in range(len(image)):
        if '#' not in image[i]:
            expanding_rows.append(i)

    # Locate all galaxies
    galaxies = []
    for y, row in enumerate(image):
        for x, space in enumerate(row):
            if space == '#':
                galaxies.append((x, y))

    res = 0
    for (ax, ay), (bx, by) in product(galaxies):
        res += 999_999 * len([1 for x in expanding_cols if ax < x < bx or bx < x < ax])
        res += 999_999 * len([1 for y in expanding_rows if ay < y < by or by < y < ay])
        res += abs(ax - bx) + abs(ay - by)

    print(res)

if __name__ == '__main__':
    main()
