import re

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
cfields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

re_yr = re.compile('^\d{4}$')
re_ht = re.compile('^\d+(in|cm)$')
re_hc = re.compile('^\#(\d|[a-f]){6}$')
ls_ec = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
re_pi = re.compile('^\d{9}$')


def passport_init(fields):
	p = {}
	for f in fields:
		p[f] = None
	return p


def passport_check(p, fields):
	for f in fields:
		if p[f] == None:
			return False
	return True


def passport_valid(p):
	# byr (Birth Year) - four digits; at least 1920 and at most 2002.
	if not (re_yr.match(p['byr']) and
			int(p['byr'])>=1920 and
			int(p['byr'])<=2002):
		return False
	
	# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
	if not (re_yr.match(p['iyr']) and
			int(p['iyr'])>=2010 and
			int(p['iyr'])<=2020):
		return False

	#eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
	if not (re_yr.match(p['eyr']) and
			int(p['eyr'])>=2020 and
			int(p['eyr'])<=2030):
		return False

	#hgt (Height) - a number followed by either cm or in:
		#If cm, the number must be at least 150 and at most 193.
		#If in, the number must be at least 59 and at most 76.
	if not re_ht.match(p['hgt']):
		return False
	else:
		if p['hgt'][-2:] == 'cm':
			if not (int(p['hgt'][:-2])>=150 and
					int(p['hgt'][:-2])<=193):
				return False
		elif p['hgt'][-2:] == 'in':
			if not (int(p['hgt'][:-2])>=59 and
					int(p['hgt'][:-2])<=76):
				return False


	#hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
	if not re_hc.match(p['hcl']):
		return False

	#ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
	if p['ecl'] not in ls_ec:
		return False

	#pid (Passport ID) - a nine-digit number, including leading zeroes.
	if not re_pi.match(p['pid']):
		return False

	#cid (Country ID) - ignored, missing or not.


	return True





with open('input.txt') as file:

	passports = []

	p = passport_init(fields)

	for l in list(file):
		if l == '\n':
			passports.append(p)
			p = passport_init(fields)
		else:
			data = [d.split(':') for d in l.strip('\n').split(' ')]
			for d in data:
				p[d[0]] = d[1]
	passports.append(p)

	print('Total passports: ', len(passports))

	good = 0
	for p in passports:
		if passport_check(p, cfields) and passport_valid(p):
			good += 1
			#print(p)

	print('Valid passports: ', good)


file.close()
