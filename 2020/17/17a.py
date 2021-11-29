def count_near(x0,y0,z0):
	count = 0
	for x in range(x0-1,x0+2):
		for y in range(y0-1,y0+2):
			for z in range(z0-1,z0+2):
				if not (x==x0 and y==y0 and z==z0):
					if data[z][y][x] == '#':
						count += 1

	return count


def step():
	xm, ym, zm = len(data[0][0]), len(data[0]), len(data)
	mat = [[['.' for x in range(xm)] for y in range(ym)] for z in range(zm)]
	for z in range(1,len(data)-1):
		for y in range(1,len(data[z])-1):
			for x in range(1,len(data[z][y])-1):
				if data[z][y][x] == '.':
					if count_near(x,y,z) == 3:
						mat[z][y][x] = '#'
					else:
						mat[z][y][x] = '.'
				elif data[z][y][x] == '#':
					if count_near(x,y,z) in (2,3):
						mat[z][y][x] = '#'
					else:
						mat[z][y][x] = '.'

	mat_copy(mat, data)
	print(' ******* STEP ******* ')


def mat_copy(f,t):
	for z in range(len(f)):
		for y in range(len(f[z])):
			for x in range(len(f[z][y])):
				t[z][y][x] = f[z][y][x]



def data_print():
	for z in range(len(data)):

		print('\nz = ' + str(z-p))
		for y in range(len(data[z])):
			print(''.join(data[z][y]))


def data_count():
	count = 0
	for z in data:
		for y in z:
			for x in y:
				if x == '#':
					count += 1

	return count


p = 10

with open('input.txt') as file:
	d = [l.strip('\n') for l in list(file)]

	m = len(d)
	data = [[['.' for x in range(m+2*p)] for y in range(m+2*p)] for z in range(1+2*p)]

	for x in range(m):
		for y in range(m):
			data[p][y+p][x+p] = '#' if d[y][x]=='#' else '.'


for t in range(6):
	step()

print(data_count())


