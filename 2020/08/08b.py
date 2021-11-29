with open('input.txt') as file:
	program = []
	for l in list(file):
		program.append([l[:3], int(l[4:])])
	program.append(['eof', 0])

swap = 0
more = True

while more:
	#print(swap)
	stop = False

	acc = 0
	pc = 0
	executed = []

	while (not stop) and (pc not in executed):
		executed.append(pc)

		if (program[pc][0] == 'nop' and not swap == pc) or \
		(program[pc][0] == 'jmp' and swap == pc):
			pc += 1
		elif program[pc][0] == 'acc':
			acc += program[pc][1]
			pc += 1
		elif (program[pc][0] == 'jmp' and not swap == pc) or \
			 (program[pc][0] == 'nop' and swap == pc):
			pc += program[pc][1]
		elif program[pc][0] == 'eof':
			stop = True
			more = False

		
	swap += 1

	if swap > len(program):
		print('ERROR')
		break

print(program[pc][0])
print('acc = ' + str(acc))
print('err = ' + str(swap-1))