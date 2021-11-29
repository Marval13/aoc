from itertools import product

def neigh(m, x, y):
	ax = [x-1, x, x+1]
	ay = [y-1, y, y+1]
	n = []	

	for j in [a for a in ay if a>=0 and a<len(m)]:
		for i in [a for a in ax if a>=0 and a<len(m[j])]:
			if not (i==x and j==y):
				n.append(m[j][i])

	return n


def good(m, x, y):
	if x < 0 or x > len(m[0])-1:
		return False
	if y < 0 or y > len(m)-1:
		return False
	return True



def neigh2(m, x, y):
	d = [a for a in product([-1,0,1], repeat=2) if not a==(0,0)]

	n = []

	for (dx, dy) in d:
		#print(dx, dy)
		sx, sy = x, y
		sx += dx
		sy += dy

		while good(m, sx, sy):
			if not m[sy][sx] == '.':
				n.append(m[sy][sx])
				break
			sx += dx
			sy += dy

	return n




	# y
	#n.append(min([M] + [a for a in range(len(m[y])) if (a>x and m[y][a]=='#')]))
	#n.append(max([-1] + [a for a in range(len(m[y])) if (a<x and m[y][a]=='#')]))

	# cleanup
	#n = [a for a in n if not a == -1]

	#return n


def step(m):
	n = []
	for y in range(len(m)):
		l = []
		for x in range(len(m[y])):
			if m[y][x] == '.':
				c = '.'
			elif neigh2(m, x, y).count('#') == 0:
				c = '#'
			elif neigh2(m, x, y).count('#') > 4:
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

