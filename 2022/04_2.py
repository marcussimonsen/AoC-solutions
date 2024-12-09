import sys

def overlaps(a1, a2, b1, b2):
    return b1 <= a2 and b2 >= a1

lines = sys.stdin.readlines()

count = 0

for line in lines:
    elf1, elf2 = line.split(',')
    elf1_1, elf1_2 = [int(i) for i in elf1.split('-')]
    elf2_1, elf2_2 = [int(i) for i in elf2.split('-')]

    if overlaps(elf1_1, elf1_2, elf2_1, elf2_2):
        count += 1

print(count)