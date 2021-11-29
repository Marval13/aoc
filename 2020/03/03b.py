
with open('input.txt') as file:
	data = [l.strip('\n') for l in list(file)]
	my = len(data)
	mx = len(data[0])

	slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]

	trees = []

	for s in slopes:
		x, y = 0, 0
		t = 0

		while y < my:
			if data[y][x] == '#':
				t += 1

			y += s[1]
			x = (x + s[0]) % mx

		trees.append(t)

	print(trees)
	tot = 1
	for t in trees:
		tot *= t

	print(tot)

file.close()