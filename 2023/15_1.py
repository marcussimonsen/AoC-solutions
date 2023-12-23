#!/usr/bin/python3

from functools import reduce

def h(s):
    return reduce(lambda acc, x: (acc + ord(x)) * 17 % 256, s, 0)

def main():
    sequence = input().strip().split(',')
    res = sum([h(i) for i in sequence])
    print(res)

if __name__ == '__main__':
    main()
