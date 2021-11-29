with open("input.txt") as file:
	data = list(file.readlines())

	count = 0

	for d in data:
		rule, pw = d.split(": ")
		mima, ch = rule.split(" ")
		mi, ma = mima.split("-")
		mi, ma = int(mi)-1, int(ma)-1
		pw = pw.strip("\n")

		if (pw[mi] == ch or pw[ma] == ch) and not (pw[mi] == ch and pw[ma] == ch):
			count+=1
			#print(ch, pw[mi], pw[ma])

	print(count)

file.close()