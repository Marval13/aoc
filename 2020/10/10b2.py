def reduce(l):
	count = 0
	for i in range(1,len(l)-1):
		if l[i+1]-l[i-1]<=3:
			count += reduce(l[i-1:i]+l[i+1:])
	return count + 1


with open('input.txt') as file:
	data = []
	for l in list(file):
		data.append(int(l))

data.sort()
data = [0] + data + [max(data)+3]

a = 0
x = 0
i = 0

clusters = []

for j in range(1,len(data)):
	b = data[j]
	if b-x == 3:
		clusters.append(data[i:j])
		a = b
		i=j
	x = b

print(clusters)


total = 1
for c in clusters:
	total *= reduce(c)

print(total)
