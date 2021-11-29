target = 'shiny gold'

with open('input.txt') as file:
	
	rules = {}

	for l in list(file):
		b, rs = l.strip('.\n').split(' contain ')
		if not rs == 'no other bags':
			r = [rn[2:] for rn in rs.split(', ')]
			rules[b.replace(' bags','')] = [a.replace(' bags','').replace(' bag','') for a in r]

checked = False
good = []

while not checked:
	checked = True
	for b,r in rules.items():
		for bag in r:
			if (bag in good or bag == target) and b not in good:
				good.append(b)
				checked = False

print(len(good))