ops = ['+', '*']

def sy(l):
	o = []
	stack = []
	for c in l:
		if c == '(':
			stack.append(c)
		elif c == ')':
			while not stack[len(stack)-1] == '(':
				o.append(stack.pop())
			stack.pop()
		elif c in ops:
			if len(stack) == 0 or stack[len(stack)-1] == '(':
				stack.append(c)
			else:
				o.append(stack.pop())
				stack.append(c)
		else:
			o.append(c)
	o.extend(stack)

	return(o)


def ev(l):
	stack = []
	for c in l:
		if c =='+':
			stack.append(stack.pop() + stack.pop())
		elif c =='*':
			stack.append(stack.pop() * stack.pop())
		else:
			stack.append(int(c))

	return stack.pop()




with open('input.txt') as file:
	data = []
	for l in list(file):
		e = []
		for d in l.strip('\n').split(' '):
			e.extend([c for c in d])
		data.append(e)

	print(sum(ev(sy(l)) for l in data))




