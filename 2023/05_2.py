#!/usr/bin/python3
import sys
from functools import reduce

def main():
    lines = sys.stdin.readlines()
    seeds = [int(seed) for seed in lines[0][6::].strip().split()]

    it = iter(seeds)
    seeds = []
    for seed in it:
        seeds.append((seed, next(it)))

    dsts, srcs, lens = [], [], []
    i = 2
    for j in range(7):
        i += 1
        dsts.append([])
        srcs.append([])
        lens.append([])
        while i < len(lines) and len(lines[i].strip()) != 0:
            dst, src, length = lines[i].strip().split()
            dsts[j].append(int(dst))
            srcs[j].append(int(src))
            lens[j].append(int(length))
            i += 1
        i += 1

    current = seeds
    for i in range(7):
        new = []
#        print(i)
#        print(current)
        while len(current) != 0:
            c, r = current.pop()
            found = False
            for src, dst, length in zip(srcs[i], dsts[i], lens[i]):
                if c + r > src and c < src + length:
                    s = dst + c - src
                    t = r
                    if c + r > src + length:
                        t -= c + r - (src + length)
                    if c < src:
                        s += src - c
                        t -= src - c
                    if s < 0:
                        t -= abs(s)
                        s = 0
                        if t <= 0:
                            continue
                    new.append((s, t))
                    if c + r > src + length:
                        current.append((src + length, c + r - (src + length)))
                    if c < src:
                        current.append((c, src - c))
                    found = True
                    break
            if not found:
                new.append((c, r))
        current = new

    print(min([c for c, r in current]))

if __name__ == '__main__':
    main()
