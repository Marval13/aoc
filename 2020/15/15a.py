test = [0,3,6]
data = [2,0,1,7,4,14,18]


li = data

lut = {}

for i in range(len(li)-1):
	lut[li[i]] = i

last = li[-1]

for i in range(len(li)-1, 30000000-1):
	if last in lut:
		t = i-lut[last]
	else:
		t = 0

	lut[last] = i
	last = t

	#print(i)

#print(lut)
print(last)







