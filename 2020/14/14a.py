def apply_mask(n, m):
	mand = int(m.replace('X','1'), 2)
	mor = int(m.replace('X','0'), 2)
	return (n & mand) | mor

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
mask = 0

for op in data:
	if op[0] == 'MSK':
		mask = op[1]
	elif op[0] == 'ASS':
		mem[op[1]] = apply_mask(op[2], mask)

#print(mem)

print(sum(mem.values()))