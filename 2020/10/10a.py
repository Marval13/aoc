with open('input.txt') as file:
	data = []
	for l in list(file):
		data.append(int(l))

diff1 = 0
diff3 = 0

data.sort()

a = 0

for b in data:
	#print(a, b, b-a)
	if b-a == 1:
		diff1 += 1
	elif b-a == 3:
		diff3 += 1
	a = b

diff3 += 1

print(diff1, diff3)
print(diff1 * diff3)