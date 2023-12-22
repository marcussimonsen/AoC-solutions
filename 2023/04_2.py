#!/usr/bin/python3

import sys

def main():
    lines = sys.stdin.readlines()
    cards = [1 for _ in range(len(lines))]
    for i, line in enumerate(lines):
        card, winning_numbers = line.strip().split("|")
        _, card_numbers = card.strip().split(":")
        card_numbers = [int(num) for num in card_numbers.strip().split()]
        winning_numbers = [int(num) for num in winning_numbers.strip().split()]
        j = i+1
        for num in card_numbers:
            if num in winning_numbers:
                cards[j] += cards[i]
                j += 1

    print(sum(cards))

if __name__ == "__main__":
    main()
