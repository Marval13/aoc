full = set([c for c in 'qwertyuiopasdfghjklzxcvbnm'])

with open('input.txt') as file:

	groups = []

	g = full

	for l in list(file):
		if l =='\n':
			groups.append(g)
			g = full
		else:
			g = g.intersection(set([i for i in l.strip('\n')]))
	groups.append(set(g))

	#print(groups)
	count = 0
	for g in groups:
		count += len(g)

	print(count)

