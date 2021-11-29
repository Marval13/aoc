with open('input.txt') as file:
	program = []
	for l in list(file):
		program.append([l[:3],int(l[4:])])


acc = 0
pc = 0
executed = []

while pc not in executed:
	executed.append(pc)
	if program[pc][0] == 'nop':
		pc += 1
	elif program[pc][0] == 'acc':
		acc += program[pc][1]
		pc += 1
	elif program[pc][0] == 'jmp':
		pc += program[pc][1]


print(acc)