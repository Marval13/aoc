def check(bus, n):
	for b in bus:
		#print('\t' + str((t+b[1]) % b[0]))
		if not (t + b[1]) % b[0] == 0:
			return False
	return True


with open('input.txt') as file:
	file.readline()
	data = []
	for b in file.readline().strip('\n').split(','):
		if b == 'x':
			data.append(1)
		else:
			data.append(int(b))

data = [[b, data.index(b)] for b in data if not b == 1]


step = 1
t = 0
todo = data
stop = False

while todo:
	print(t)
	t += step
	if check([todo[0]], t):
		step *= todo[0][0]
		del todo[0]

print(t)
