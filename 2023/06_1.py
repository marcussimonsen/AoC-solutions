#!/usr/bin/python3
from functools import reduce

def main():
    times = [int(time) for time in input().split()[1:]]
    distances = [int(distance) for distance in input().split()[1:]]

    ways_to_win = []
    for i, (time, distance) in enumerate(zip(times, distances)):
        ways_to_win.append(0)
        for speed in range(time):
            if speed * (time - speed) > distance:
                ways_to_win[i] += 1
    print(reduce(lambda a, b: a * b, ways_to_win))

if __name__ == "__main__":
    main()
