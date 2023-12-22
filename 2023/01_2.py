#!/usr/bin/python3
import sys

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers_rev = [n[::-1] for n in numbers]

def first_digit(s, words):
    digit_index = -1
    digit = None
    for i, c in enumerate(s):
        if c.isdigit():
            digit_index = i
            digit = c
            break
    for i, word in enumerate(words):
        idx = s.find(word)
        if idx != -1 and idx < digit_index:
            digit_index = idx
            digit = "" + str(i+1)
    return digit


def main():
    nums = [int(first_digit(line, numbers) + first_digit(line[::-1], numbers_rev)) for line in sys.stdin]
    print(nums[-1])
    print(sum(nums))

if __name__ == '__main__':
    main()
