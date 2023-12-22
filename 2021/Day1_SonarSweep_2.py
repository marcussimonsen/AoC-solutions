# Function calculating sum of three numbers
def calcSum(num1, num2, num3):
    return num1 + num2 + num3

with open('Day1_SonarSweep_Input.txt') as f:
    lines = f.readlines()

    increases = 0
    lastNumber_1 = int(lines[0])
    lastNumber_2 = int(lines[1])
    lastSum = calcSum(int(lines[2]), lastNumber_1, lastNumber_2)

    for x in range(3, len(lines)):
        # Get number and calculate sum
        number = int(lines[x])
        currentSum = calcSum(number, lastNumber_1, lastNumber_2)

        # Count increase
        if currentSum > lastSum:
            increases += 1

        # Saving values for next iteration
        lastNumber_2 = lastNumber_1
        lastNumber_1 = number
        lastSum = currentSum

    # Print result
    print(increases)