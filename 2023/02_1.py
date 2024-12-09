#!/usr/bin/python3
import sys
import re

max_reds = 12
max_greens = 13
max_blues = 14


def main():
    legal = []
    for line in sys.stdin:
        game, counts = line.strip().split(": ")
        _, game = game.split()
        game = int(game)
        legal.append(game)
        counts = re.split("[,;] ", counts)
        for count in counts:
            num, color = count.split()
            if color == "red" and int(num) > max_reds:
                if game in legal:
                    legal.remove(game)
            elif color == "green" and int(num) > max_greens:
                if game in legal:
                    legal.remove(game)
            elif color == "blue" and int(num) > max_blues:
                if game in legal:
                    legal.remove(game)

    print(sum(legal))


if __name__ == "__main__":
    main()
