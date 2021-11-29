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