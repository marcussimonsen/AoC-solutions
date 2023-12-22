with open('Day3_BinaryDiagnostic_Input.txt') as input:
    binaryNumbers = input.readlines()
    
    # List with specified size from input file
    binaries = ['' for x in range(len(binaryNumbers[0])-1)]

    # Binary conversion to vertical from horizontal input
    for binary in binaryNumbers:
        for bit in range(len(binary)-1):
            binaries[bit] += binary[bit]
    
    gammaRate = ''
    epsilonRate = ''

    for binary in binaries:
        if binary.count('1') > len(binary)/2:
            gammaRate += '1'
            epsilonRate += '0'
        else:
            gammaRate += '0'
            epsilonRate += '1'
    
    gamma = int(gammaRate, base=2)
    epsilon = int(epsilonRate, base=2)

    print('Gamma rate: ' + str(gamma))
    print('Epsilon rate: ' + str(epsilon))
    print('Power consumption: ' + str(gamma * epsilon))