def containsDouble(lst):
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            if lst[i] == lst[j]:
                return True
    return False

line = input()
line = line.strip()

marker = []
i = 0

for char in line:
    i += 1
    marker.append(char)
    if len(marker) > 4:
        marker.pop(0)
    if len(marker) == 4 and not containsDouble(marker):
        break
print(i)