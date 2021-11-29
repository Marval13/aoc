class Boat(object):
	x = 0
	y = 0
	d = 0
	
	dirs = ['E', 'N', 'W', 'S']

	def pos(self):
		return [self.x, self.y]


	def move(self, l):
		c, n = l

		if c == 'F':
			c = self.dirs[self.d]

		if c == 'L':
			self.d = (self.d + n//90) % 4
		elif c == 'R':
			self.d = (self.d - n//90) % 4
		elif c == 'E':
			self.x += n
		elif c == 'N':
			self.y += n
		elif c == 'W':
			self.x -= n
		elif c == 'S':
			self.y -= n


with open('input.txt') as file:
	data = []
	for l in list(file):
		data.append([l[0], int(l[1:])])

b = Boat()

for l in data:
	b.move(l)

print(b.pos())
print(sum(abs(x) for x in b.pos()))