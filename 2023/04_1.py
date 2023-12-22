#!/usr/bin/python3

import sys

def main():
    lines = sys.stdin.readlines()
    points = 0
    for line in lines:
        card, winning_numbers = line.strip().split("|")
        _, card_numbers = card.strip().split(":")
        card_numbers = [int(num) for num in card_numbers.strip().split()]
        winning_numbers = [int(num) for num in winning_numbers.strip().split()]
        card_points = 0
        for num in card_numbers:
            if num in winning_numbers:
                if card_points == 0:
                    card_points = 1
                else:
                    card_points *= 2
        points += card_points

    print(points)

if __name__ == "__main__":
    main()
