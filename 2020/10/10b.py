# This works, but it is incredibly slow

import sys

def reduce_slow(l):
	if l in red:
		return 0
	red.append(l)
	for i in range(1,len(l)-1):
		if l[i+1]-l[i-1]<=3:
			reduce_slow(l[:i]+l[i+1:])
	return 0


def reduce(l):
	count = 0
	#red.append(l)
	for i in range(1,len(l)-1):
		if l[i+1]-l[i-1]<=3:
			count += reduce(l[i-1:i]+l[i+1:])
	return count + 1


def reduce1(l):
	count = 0
	for i in range(1,len(l)-1):
		print(i)
		if l[i+1]-l[i-1]<=3:
			count += reduce(l[i-1:i]+l[i+1:])
	return count + 1


with open(sys.argv[1]) as file:
	data = []
	for l in list(file):
		data.append(int(l))

data.sort()

data = [0] + data + [max(data) + 3]

red = []

#reduce(data)

#print(red)

print(reduce1(data))
#print('Red: ' + str(len(red)))

