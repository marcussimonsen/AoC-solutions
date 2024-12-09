#!/usr/bin/python3
import sys
from enum import Enum

clas Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Tile:
    def __init__(self, c):
        self.c = c
        self.visited = False
        self.visited_from = []

def main():
    contraption = [list(line.strip() for line in sys.stdin.readlines())]

if __name__ == '__main__':
    main()
