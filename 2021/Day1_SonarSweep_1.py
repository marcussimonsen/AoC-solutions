with open('Day1_SonarSweep_Input.txt') as f:
    lines = f.readlines()

    increases = 0
    lastNumber = int(lines[0])

    for x in lines:
        x = int(x)
        if x > lastNumber:
            increases += 1
        lastNumber = x

    print(increases)