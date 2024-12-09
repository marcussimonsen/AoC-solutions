from os import defpath


with open('Day2_Dive_Input.txt') as input:
    lines = input.readlines()

    horizontal = 0
    depth = 0
    aim = 0

    for command in lines:
        direction, magnitude = command.split(' ')

        change = int(magnitude)

        if direction == 'forward':
            horizontal += change
            depth += aim * change
        elif direction == 'down':
            aim += change
        elif direction == 'up':
            aim -= change
    
    print('Horizontal position: ' + str(horizontal))
    print('Vertical position: ' + str(depth))
    print('Distance: ' + str(horizontal * depth))