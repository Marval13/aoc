class Mask(object):
	def __init__(self, s):
		super(Mask, self).__init__()
		self.r = [c for c in s]
		self.d = self.compute(self.r)

	def raw(self):
		return(''.join(self.r))

	def data(self):
		return self.d
		
	def compute(self, l):
		ms = []
		if l.count('X')>0:
			i = l.index('X')
			l0, l1 = l[:], l[:]
			l0[i], l1[i] = '0', '1'
			ms = ms + self.compute(l0)
			ms = ms + self.compute(l1)
			return ms
		else:
			#print(l)
			return [int(''.join(l), 2)]


	def apply(self, n):
		n1 = [c for c in format(n, '036b')]

		for i in range(36):
			if not self.r[i] == '0':
				n1[i] = self.r[i]

		return self.compute(n1)





with open('input.txt') as file:
	data = []
	for l in list(file):
		if l[:3] == 'mas':
			m = l[7:].strip('\n')
			data.append(['MSK', m])
		else:
			v = l[4:].strip('\n').split('] = ')
			data.append(['ASS', int(v[0]), int(v[1])])


mem = {}

for op in data:
	if op[0] == 'MSK':
		mask = Mask(op[1])
	elif op[0] == 'ASS':
		for m in mask.apply(op[1]):
			mem[m] = op[2]

#print(mem)

print(sum(mem.values()))