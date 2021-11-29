with open('input.txt') as file:

	groups = []

	g = []

	for l in list(file):
		if l =='\n':
			groups.append(set(g))
			g = []
		else:
			g = g + [i for i in l.strip('\n')]
	groups.append(set(g))

	#print(groups)
	count = 0
	for g in groups:
		count += len(g)

	print(count)

