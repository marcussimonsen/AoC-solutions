with open('TestInput.txt') as input:
    lines = input.readlines()

    # All numbers drawn
    numbers = lines[0].split(',')

    # List holding all plates
    plates = []

    line = 2

    while line < len(lines):
        plate = []

        for l in lines[line:line+5]:
            for number in l.replace('  ', ' ').replace('\n', '').split(' '):
                print('Added number: ' + number)
                plate.append(number)

        line += 5
        plates.append(plate)

    for plate in plates:
        print('New plate')
        for number in plate:
            print(number)