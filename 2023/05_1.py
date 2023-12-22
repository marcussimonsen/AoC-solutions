#!/usr/bin/python3
import sys

def main():
    lines = sys.stdin.readlines()
    seeds = [int(seed) for seed in lines[0][6::].strip().split()]

    i = 2
    for _ in range(7):
        i += 1
        dsts, srcs, lens = [], [], []
        while i < len(lines) and len(lines[i].strip()) != 0:
            dst, src, length = lines[i].strip().split()
            dsts.append(int(dst))
            srcs.append(int(src))
            lens.append(int(length))
            i += 1
        for j, seed in enumerate(seeds):
            for dst, src, length in zip(dsts, srcs, lens):
                if seed >= src and seed < src + length:
                    seeds[j] = dst + seed - src
                    break
        i += 1

    print(min(seeds))

if __name__ == '__main__':
    main()
