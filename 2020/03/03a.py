
with open('input.txt') as file:
	data = [l.strip('\n') for l in list(file)]

	my = len(data)
	mx = len(data[0])

	#print(data)

	x, y = 0, 0
	trees = 0

	while y < my:
		if data[y][x] == '#':
			trees += 1

		y += 1
		x = (x + 3) % mx

	print(trees)

file.close()