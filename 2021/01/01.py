with open('input.txt') as file:
    data = []
    for l in list(file):
        data.append(int(l))

sincrements = 0
for i in range(0, len(data) - 1):
    if data[i] < data[i + 1]:
        sincrements += 1

print("Single increments", sincrements)

def window(list, index, length):
    return sum([list[i] for i in range(index, index + length)])

wincrements = 0
for i in range(0, len(data) - 3):
    if window(data, i, 3) < window(data, i + 1, 3):
        wincrements += 1

print("Triple increments", wincrements)
