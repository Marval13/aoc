class Boat(object):
	x, y = 0, 0
	d = 0
	
	wx, wy = 10, 1


	dirs = ['E', 'N', 'W', 'S']

	def pos(self):
		return [self.x, self.y]


	def wpos(self):
		return [self.wx, self.wy]


	def move(self, l):
		c, n = l

		if c == 'F':
			self.x += self.wx * n
			self.y += self.wy * n
		elif c == 'L':
			for i in range(n//90):
				self.wx, self.wy = -self.wy, self.wx
		elif c == 'R':
			for i in range(n//90):
				self.wx, self.wy = self.wy, -self.wx
		elif c == 'E':
			self.wx += n
		elif c == 'N':
			self.wy += n
		elif c == 'W':
			self.wx -= n
		elif c == 'S':
			self.wy -= n


with open('input.txt') as file:
	data = []
	for l in list(file):
		data.append([l[0], int(l[1:])])

b = Boat()

for l in data:
	#print(b.pos(), b.wpos())
	b.move(l)


print(b.pos(), b.wpos())
print(sum(abs(x) for x in b.pos()))