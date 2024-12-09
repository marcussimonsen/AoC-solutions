with open('Day2_Dive_Input.txt') as input:
    lines = input.readlines()

    horizontal = 0
    depth = 0

    for command in lines:
        direction, magnitude = command.split(' ')

        if direction == 'forward':
            horizontal += int(magnitude)
        elif direction == 'down':
            depth += int(magnitude)
        elif direction == 'up':
            depth -= int(magnitude)
    
    print('Horizontal position: ' + str(horizontal))
    print('Vertical position: ' + str(depth))
    print('Distance: ' + str(horizontal * depth))