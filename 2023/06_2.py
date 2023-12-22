#!/usr/bin/python3
from functools import reduce

def main():
    time = int(reduce(lambda a, b: a + b, input().split()[1:]))
    distance = int(reduce(lambda a, b: a + b, input().split()[1:]))

    # dist = (time - speed) * speed
    # dist = time * speed - speed * speed
    # speed * speed - time * speed + dist = 0
    # speed = (time +- sqrt(time * time - 4 * dist)) / 2
    
    speed0 = int((time - (time * time - 4 * distance) ** 0.5) / 2)
    speed1 = int((time + (time * time - 4 * distance) ** 0.5) / 2)

    print(speed1 - speed0)

if __name__ == "__main__":
    main()
