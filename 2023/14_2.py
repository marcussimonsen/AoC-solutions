#!/usr/bin/python3
import sys

def roll_north(notes):
    for y in range(len(notes)):
        for x in range(len(notes[y])):
            if notes[y][x] == 'O':
                dy = y
                while dy > 0 and notes[dy-1][x] == '.':
                    dy -= 1
                notes[y][x] = '.'
                notes[dy][x] = 'O'

def roll_south(notes):
    for y in reversed(range(len(notes))):
        for x in range(len(notes[y])):
            if notes[y][x] == 'O':
                dy = y
                while dy < len(notes)-1 and notes[dy+1][x] == '.':
                    dy += 1
                notes[y][x] = '.'
                notes[dy][x] = 'O'

def roll_west(notes):
    for x in range(len(notes[0])):
        for y in range(len(notes)):
            if notes[y][x] == 'O':
                dx = x
                while dx > 0 and notes[y][dx-1] == '.':
                    dx -= 1
                notes[y][x] = '.'
                notes[y][dx] = 'O'

def roll_east(notes):
    for x in reversed(range(len(notes[0]))):
        for y in range(len(notes)):
            if notes[y][x] == 'O':
                dx = x
                while dx < len(notes[0])-1 and notes[y][dx+1] == '.':
                    dx += 1
                notes[y][x] = '.'
                notes[y][dx] = 'O'

def cycle(notes):
    roll_north(notes)
    roll_west(notes)
    roll_south(notes)
    roll_east(notes)

def main():
    notes = [list(line.strip()) for line in sys.stdin.readlines()]

    # Roll rocks
    for i in range(1_000_000_000):
        cycle(notes)
        if i % 100_000 == 0:
            print(i)

    # Calculate load
    load = 0
    for y in range(len(notes)):
        for x in range(len(notes[y])):
            if notes[y][x] == 'O':
                load += len(notes) - y

    print(load)

if __name__ == '__main__':
    main()
