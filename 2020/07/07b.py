target = 'shiny gold'

def count_bags(rules, color):
	total = 0
	if color not in rules:
		return 1

	for b, n in rules[color].items():
		total += n * count_bags(rules, b)
	return total + 1


with open('input.txt') as file:
	
	rules = {}

	for l in list(file):
		b, rs = l.strip('.\n').split(' contain ')
		if not rs == 'no other bags':
			r = {rn[2:].replace(' bags','').replace(' bag',''):int(rn[0]) 
				 for rn in rs.split(', ')}
			rules[b.replace(' bags','')] = r

print(count_bags(rules, target) - 1)
