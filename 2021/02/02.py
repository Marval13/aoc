with open('input.txt') as file:
    data = []
    for l in list(file):
        a, b = l.split(" ")
        data.append((a, int(b)))

# Part One

depth = 0
distance = 0

for line in data:
    if line[0] == "forward":
        distance += line[1]
    elif line[0] == "down":
        depth += line[1]
    elif line[0] == "up":
        depth -= line[1]

print("Part one")
print(distance, depth)
print(distance * depth)

# Part Two

aim = 0
depth = 0
distance = 0

for line in data:
    if line[0] == "forward":
        distance += line[1]
        depth += line[1] * aim
    elif line[0] == "down":
        aim += line[1]
    elif line[0] == "up":
        aim -= line[1]

print("Part two")
print(distance, depth)
print(distance * depth)
