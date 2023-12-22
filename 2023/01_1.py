#!/usr/bin/python3
import sys

def first_digit(s):
    for c in s:
        if c.isdigit():
            return c

def main():
    nums = [int(first_digit(line) + first_digit(line[::-1])) for line in sys.stdin]
    print(sum(nums))

if __name__ == '__main__':
    main()
