#!/usr/bin/python3

import sys
from itertools import repeat

def get_unknown(springs):
    for i, x in enumerate(springs):
        if x == '?':
            yield i

def matches(springs, inserts, groups):
    actual_groups = []
    i = 0
    while i < len(springs):
        group = 0
        while i < len(springs) and (springs[i] == '#' or i in inserts):
            i += 1
            group += 1
        if group != 0:
            actual_groups.append(group)
        i += 1
    return actual_groups == groups

def main():
    lines = sys.stdin.readlines()
    arrangements = [0] * len(lines)
    for l, line in enumerate(lines):
        springs, groups = line.strip().split()
        springs = list(springs)
        springs.append('?')
        springs = list(repeat(springs, 5))[:-1]

        groups = [int(x) for x in groups.split(',')]

        print(springs)
        unknown = list(get_unknown(springs))

        for i in range(2**len(unknown)):
            inserts = []
            for j in range(len(unknown)):
                if i & (1 << j):
                    inserts.append(unknown[j])
            if matches(springs, inserts, groups):
                arrangements[l] += 1

    print(sum(arrangements))

if __name__ == '__main__':
    main()
