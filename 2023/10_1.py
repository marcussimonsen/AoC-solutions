#!/usr/bin/python3
import sys
from collections import deque

NORTH = 0,
EAST = 1,
SOUTH = 2,
WEST = 3


def find_start(tiles):
    for y, line in enumerate(tiles):
        for x, tile in enumerate(line):
            if tile == 'S':
                return x, y
    print('no start')
    print(tiles)
    sys.exit(1)

def other_direction(direction, tile):
    if tile == '|':
        return (NORTH if direction == SOUTH else SOUTH)
    if tile == '-':
        return (EAST if direction == WEST else WEST)
    if tile == 'L':
        return (NORTH if direction == EAST else EAST)
    if tile == 'J':
        return (NORTH if direction == WEST else WEST)
    if tile == '7':
        return (SOUTH if direction == WEST else WEST)
    if tile == 'F':
        return (SOUTH if direction == EAST else EAST)
    return None

def main():
    tiles = [list(line.strip()) for line in sys.stdin]

    sx, sy = find_start(tiles)

    starts = []

    if sy > 0 and tiles[sy-1][sx] in ['7', '|', 'F']:
        starts.append((sx, sy-1, 1, other_direction(SOUTH, tiles[sy-1][sx])))
    if sy < len(tiles) - 1 and tiles[sy+1][sx] in ['J', '|', 'L']:
        starts.append((sx, sy+1, 1, other_direction(NORTH, tiles[sy+1][sx])))
    if sx > 0 and tiles[sy][sx-1] in ['F', '-', 'L']:
        starts.append((sx-1, sy, 1, other_direction(EAST, tiles[sy][sx-1])))
    if sx < len(tiles[0]) - 1 and tiles[sy][sx+1] in ['J', '-', '7']:
        starts.append((sx+1, sy, 1, other_direction(WEST, tiles[sy][sx+1])))

    queue = deque(starts)

    max_dist = 0

    while queue:
        x, y, dist, direction = queue.popleft()

        if tiles[y][x] == '.':
            continue

        max_dist = max(dist, max_dist)

        if direction == NORTH:
            queue.append((x, y-1, dist+1, other_direction(SOUTH, tiles[y-1][x])))
        if direction == SOUTH:
            queue.append((x, y+1, dist+1, other_direction(NORTH, tiles[y+1][x])))
        if direction == EAST:
            queue.append((x+1, y, dist+1, other_direction(WEST, tiles[y][x+1])))
        if direction == WEST:
            queue.append((x-1, y, dist+1, other_direction(EAST, tiles[y][x-1])))

        tiles[y][x] = '.'

    print(max_dist)

if __name__ == '__main__':
    main()
