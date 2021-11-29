from itertools import permutations

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
		z.append(desc)
		rules.append(z)

	ticket = [int(i) for i in rt.strip('\n').split(',')]

	for t in rd:
		data.append([int(i) for i in t.strip('\n').split(',')])


#print(rules)
#print(ticket)
#print(data)



for t in data[:]:
	for f in t:
		good = False
		for r in rules:
			if f in range(r[0][0],r[0][1]+1) or \
			   f in range(r[1][0],r[1][1]+1):
				good = True

		if not good:
			data.remove(t)
			break


poss = [rules[:] for _ in range(len(rules))]

for t in data:
	for i in range(len(t)):
		for r in poss[i][:]:
			if not(t[i] in range(r[0][0],r[0][1]+1) or \
				   t[i] in range(r[1][0],r[1][1]+1)):
				poss[i].remove(r)


final = [[r[2] for r in p] for p in poss]

#print(final)


for i in range(20):
	for r in final:
		if len(r) == 1:
			for l in final:
				if not r == l and r[0] in l:
					l.remove(r[0])

final = [l[0] for l in final]

print(final)

mult = 1
for i in range(len(final)):
	if final[i][:9] == 'departure':
		mult *= ticket[i]

print(mult)
#print(89*73*101*53*61*113)
#3 5 8 12 15 17