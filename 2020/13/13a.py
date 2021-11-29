with open('input.txt') as file:
	dep = int(file.readline().strip('\n'))
	data = [int(b) for b in file.readline().strip('\n').split(',') if not b == 'x']

print(dep)
print(data)

diff = [(dep//b + 1) * b - dep for b in data]

bus = data[diff.index(min(diff))]

print(bus)

print(bus * min(diff))