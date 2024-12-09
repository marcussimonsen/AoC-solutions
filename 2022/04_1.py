import sys

def contains(a1, a2, b1, b2):
    return a1 <= b1 and a2 >= b2

lines = sys.stdin.readlines()

count = 0

for line in lines:
    elf1, elf2 = line.split(',')
    elf1_1, elf1_2 = [int(i) for i in elf1.split('-')]
    elf2_1, elf2_2 = [int(i) for i in elf2.split('-')]

    if contains(elf1_1, elf1_2, elf2_1, elf2_2) or contains(elf2_1, elf2_2, elf1_1, elf1_2):
        count += 1

print(count)