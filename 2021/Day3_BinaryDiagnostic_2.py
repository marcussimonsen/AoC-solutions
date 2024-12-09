def printNumbersLeft(numbers):
    for number in numbers:
        print('Binary number: ' + number)
        print('Decimal number: ' + str(int(number, base=2)))

def getBinaryTilt(binaryNumbers):
    # List with specified size from input file
    binaries = ['' for x in range(len(binaryNumbers[0])-1)]
    # Binary conversion to vertical from horizontal input
    for binary in binaryNumbers:
        for bit in range(len(binary)-1):
            binaries[bit] += binary[bit]
    
    return binaries

def calculateNumber(numbers, oneCommon, zeroCommon):
    # For every bit in the binaries
    for idx in range(len(numbers[0])):
        # Get updated tilted binary list
        binaries = getBinaryTilt(numbers)

        # Finding most common bit value
        mostCommonValue = ''
        if binaries[idx].count('1') >= len(binaries[idx])/2:
            mostCommonValue = oneCommon
        else:
            mostCommonValue = zeroCommon

        # Testing all numbers left in list for meeting criteria
        numbers = [n for n in numbers if n[idx] == mostCommonValue]

        # If only one number left, stop loop
        if len(numbers) == 1:
            break

    return numbers[0]

with open('Day3_BinaryDiagnostic_Input.txt') as input:
    binaryNumbers = input.readlines()
    
    oxygenRating = calculateNumber(binaryNumbers, '1', '0')
    co2Rating = calculateNumber(binaryNumbers, '0', '1')
    print('Oxygen rating binary: ' + str(oxygenRating))
    print('Oxygen rating decimal: ' + str(int(oxygenRating, base=2)))
    print('CO2 scrubber rating binary: ' + str(co2Rating))
    print('CO2 scrubber rating decimal: ' + str(int(co2Rating, base=2)))

    print('Life support rating: ' + str(int(oxygenRating, base=2) * int(co2Rating, base=2)))