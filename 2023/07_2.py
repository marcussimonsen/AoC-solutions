#!/usr/bin/python3
import sys
from enum import Enum
from functools import reduce
from collections import defaultdict

class HandType(Enum):
    HighCard = 0
    Pair = 1
    TwoPair = 2
    ThreeOfAKind = 3
    FullHouse = 4
    FourOfAKind = 5
    FiveOfAKind = 6

    def __lt__(self, other):
        return self.value < other.value

card_values = {
    'J': 0,
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'Q': 10,
    'K': 11,
    'A': 12
}

def get_joker_amount(hand):
    return reduce(lambda x, y: x + y, [1 if card == 'J' else 0 for card in hand])

def is_five_of_a_kind(hand):
    types = defaultdict(lambda: 0)
    jokers = get_joker_amount(hand)
    for card in hand:
        if card == 'J':
            continue
        if card in types:
            types[card] += 1
        else:
            types[card] = 1
    if len(types.keys()) > 1:
        return False
    keys = list(types.keys())
    if len(keys) == 0:
        return jokers == 5
    return types[keys[0]] + jokers == 5

def is_four_of_a_kind(hand):
    types = defaultdict(lambda: 0)
    jokers = get_joker_amount(hand)
    for card in hand:
        if card == 'J':
            continue
        if card in types:
            types[card] += 1
        else:
            types[card] = 1
    keys = list(types.keys())
    return types[keys[0]] + jokers == 4 or types[keys[1]] + jokers == 4

def is_full_house(hand):
    types = defaultdict(lambda: 0)
    jokers = get_joker_amount(hand)
    for card in hand:
        if card == 'J':
            continue
        if card in types:
            types[card] += 1
        else:
            types[card] = 1
    keys = list(types.keys())
    return types[keys[0]] + types[keys[1]] + jokers == 5 or types[keys[1]] + types[keys[0]] + jokers == 5

def is_three_of_a_kind(hand):
    types = defaultdict(lambda: 0)
    jokers = get_joker_amount(hand)
    for card in hand:
        if card == 'J':
            continue
        if card in types:
            types[card] += 1
        else:
            types[card] = 1
    if len(types.keys()) > 3:
        return False
    keys = list(types.keys())
    return types[keys[0]] + jokers == 3 or types[keys[1]] + jokers == 3 or types[keys[2]] + jokers == 3

def is_two_pair(hand):
    types = defaultdict(lambda: 0)
    jokers = get_joker_amount(hand)
    for card in hand:
        if card == 'J':
            continue
        if card in types:
            types[card] += 1
        else:
            types[card] = 1
    if len(types.keys()) > 3:
        return False
    keys = list(types.keys())
    return types[keys[0]] + types[keys[1]] + jokers == 4 or types[keys[0]] + types[keys[2]] + jokers == 4 or types[keys[1]] + types[keys[2]] + jokers == 4

def is_pair(hand):
    types = defaultdict(lambda: 0)
    jokers = get_joker_amount(hand)
    for card in hand:
        if card == 'J':
            continue
        if card in types:
            types[card] += 1
        else:
            types[card] = 1
    if len(types.keys()) > 4:
        return False
    keys = list(types.keys())
    return types[keys[0]] + jokers == 2 or types[keys[1]] + jokers == 2 or types[keys[2]] + jokers == 2 or types[keys[3]] + jokers == 2

class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.type = self.get_type()

    def __str__(self):
        return str(self.cards)

    def __repr__(self):
        return str(self.cards)

    def get_type(self):
        # Check for five of a kind
        if is_five_of_a_kind(self.cards):
            return HandType.FiveOfAKind
        # Check for four of a kind
        if is_four_of_a_kind(self.cards):
            return HandType.FourOfAKind
        # Check for full house
        if is_full_house(self.cards):
            return HandType.FullHouse
        # Check for three of a kind
        if is_three_of_a_kind(self.cards):
            return HandType.ThreeOfAKind
        # Check for two pair
        if is_two_pair(self.cards):
            return HandType.TwoPair
        # Check for pair
        if is_pair(self.cards):
            return HandType.Pair
        # Otherwise, high card
        return HandType.HighCard

    def __lt__(self, other):
        if self.type == other.type:
            i = 0
            while self.cards[i] == other.cards[i]:
                i += 1
            return card_values[self.cards[i]] < card_values[other.cards[i]]
        return self.get_type() < other.get_type()


def main():
    hands = [Hand(line.split()[0], int(line.split()[1])) for line in sys.stdin.readlines()]
    hands.sort()

    score = 0
    for i, hand in enumerate(hands):
        score += hand.bid * (i + 1)

    print(score)

if __name__ == '__main__':
    main()
