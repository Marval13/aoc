subs = [['F', '0'], ['R', '1'], ['B', '1'], ['L', '0']]

with open('input.txt') as file:
	
	passes = []
	nums = []

	for l in list(file):
		l = l.strip('\n')
		for s in subs:
			l = l.replace(s[0], s[1])
		passes.append(l)
		nums.append(int(l, 2))

	#print(passes)
	#print(nums)

	print(max(nums))

	for n in nums:
		if n+1 not in nums:
			print(n+1)

file.close()