def neigh(m, x, y):
	ax = [x-1, x, x+1]
	ay = [y-1, y, y+1]
	n = []	

	for j in [a for a in ay if a>=0 and a<len(m)]:
		for i in [a for a in ax if a>=0 and a<len(m[j])]:
			if not (i==x and j==y):
				n.append(m[j][i])

	return n


def neigh2(m, x, y):
	n = []

	# y
	n.append(min([-1] + [a for a in len(m[y]) if a>x and not m[a]=='.']))
	n.append(max([-1] + [a for a in len(m[y]) if a<x and not m[a]=='.']))

	# cleanup
	n = [a for a in n if not a == -1]

	return n


def step(m):
	n = []
	for y in range(len(m)):
		l = []
		for x in range(len(m[y])):
			if m[y][x] == '.':
				c = '.'
			elif neigh(m, x, y).count('#') == 0:
				c = '#'
			elif neigh(m, x, y).count('#') > 3:
				c = 'L'
			else:
				c = m[y][x]
			l.append(c)
		n.append(l)
	return n

with open('input.txt') as file:
	data = []
	for l in list(file):
		data.append([c for c in l.strip('\n')])




n = data
m = step(data)
i = 0



while not n == m:
	i += 1
	print(i)
	n = m
	m = step(n)

count = 0

for l in step(m):
	#print(''.join(l))
	count += l.count('#')

print(count)

