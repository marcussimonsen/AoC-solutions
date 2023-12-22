#!/usr/bin/python3
import sys

def main():
    notes = [list(line.strip()) for line in sys.stdin.readlines()]

    # Roll rocks north
    for y in range(len(notes)):
        for x in range(len(notes[y])):
            if notes[y][x] == 'O':
                dy = y
                while dy > 0 and notes[dy-1][x] == '.':
                    dy -= 1
                notes[y][x] = '.'
                notes[dy][x] = 'O'

    # Calculate load
    load = 0
    for y in range(len(notes)):
        for x in range(len(notes[y])):
            if notes[y][x] == 'O':
                load += len(notes) - y

    print(load)

if __name__ == '__main__':
    main()
