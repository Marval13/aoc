with open('input.txt') as file:
	rules = []
	ticket = []
	data = []

	f = list(file)
	rr, rt, rd = f[:f.index('\n')], f[f.index('\n')+2], f[f.index('\n')+5:]

	for r in rr:
		desc, r = r.strip('\n').split(': ')
		r = r.split(' or ')
		z = []
		for i in r:
			z.append([int(j) for j in i.split('-')])
		rules.append(z)

	ticket = [int(i) for i in rt.strip('\n').split(',')]

	for t in rd:
		data.append([int(i) for i in t.strip('\n').split(',')])


#print(rules)
#print(ticket)
#print(data)

rate = 0

for t in data:
	for f in t:
		good = False
		for r in rules:
			print(f, r)
			if f in range(r[0][0],r[0][1]+1) or \
			   f in range(r[1][0],r[1][1]+1):
			   	print('Ok')
				good = True

		if not good:
			print(f)
			rate += f


print(rate)
