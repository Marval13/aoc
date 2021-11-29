def count_near(x0,y0,z0,t0):
	count = 0
	for x in range(x0-1,x0+2):
		for y in range(y0-1,y0+2):
			for z in range(z0-1,z0+2):
				for t in range(t0-1,t0+2):
					if not (x==x0 and y==y0 and z==z0 and t == t0):
						if data[t][z][y][x] == '#':
							count += 1

	return count


def step():
	xm, ym, zm, tm = len(data[0][0][0]), len(data[0][0]), len(data[0]), len(data)
	mat = [[[['.' for x in range(xm)] for y in range(ym)] for z in range(zm)] for t in range(tm)]
	for t in range(1,len(data)-1):
		for z in range(1,len(data[t])-1):
			for y in range(1,len(data[t][z])-1):
				for x in range(1,len(data[t][z][y])-1):
					if data[t][z][y][x] == '.':
						if count_near(x,y,z,t) == 3:
							mat[t][z][y][x] = '#'
						else:
							mat[t][z][y][x] = '.'
					elif data[t][z][y][x] == '#':
						if count_near(x,y,z,t) in (2,3):
							mat[t][z][y][x] = '#'
						else:
							mat[t][z][y][x] = '.'

	mat_copy(mat, data)
	print(' ******* STEP ******* ')


def mat_copy(m0,m1):
	for z in range(len(m0)):
		for y in range(len(m0[z])):
			for x in range(len(m0[z][y])):
				for t in range(len(m0[z][y][x])):
					m1[z][y][x][t] = m0[z][y][x][t]



def data_print():
	for z in range(len(data)):

		print('\nz = ' + str(z-p))
		for y in range(len(data[z])):
			print(''.join(data[z][y]))


def data_count():
	count = 0
	for t in data:
		for z in t:
			for y in z:
				for x in y:
					if x == '#':
						count += 1

	return count


p = 8

with open('input.txt') as file:
	d = [l.strip('\n') for l in list(file)]

	m = len(d)
	data = [[[['.' for x in range(m+2*p)] for y in range(m+2*p)] for z in range(1+2*p)] for t in range(1+2*p)]

	for x in range(m):
		for y in range(m):
			data[p][p][y+p][x+p] = '#' if d[y][x]=='#' else '.'


print(data_count())

for t in range(6):
	step()
	print(data_count())

#print(data_count())


