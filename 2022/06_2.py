markerSize = 14

def containsDouble(lst):
    for i in range(markerSize):
        for j in range(markerSize):
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
    if len(marker) > markerSize:
        marker.pop(0)
    if len(marker) == markerSize and not containsDouble(marker):
        break
print(i)