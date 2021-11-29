with open("input.txt") as file:
	data = list(file.readlines())

	count = 0

	for d in data:
		rule, pw = d.split(": ")
		mima, ch = rule.split(" ")
		mi, ma = mima.split("-")
		pw = pw.strip("\n")
		l = pw.count(ch)
		if l>=int(mi) and l<=int(ma):
			count+=1
	print(count)

file.close()
