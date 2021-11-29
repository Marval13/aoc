def check_sum(n, l):
	for m in l:
		if n - m in l and not n - m == m:
			return True
	return False

preamble = 25

with open('input.txt') as file:
	data = []
	for l in list(file):
		data.append(int(l))

pos = preamble
good = True

while good:
	if check_sum(data[pos], data[pos - preamble : pos]):
		pos += 1
	else:
		good = False


print(pos, data[pos])

badpos = pos
badnum = data[pos]

pos = 0
stop = False

while not stop:
	i = 0
	tot = 0
	#print(pos, i)
	while tot < badnum:
		tot += data[pos+i]
		i += 1
		if tot == badnum:
			stop = True
	pos += 1
pos -= 1
i -= 1


print(pos, i)
print(data[pos], data[pos+i])
print(min(data[pos:pos+i+1]), max(data[pos:pos+i+1]))
print(min(data[pos:pos+i+1]) + max(data[pos:pos+i+1]))
