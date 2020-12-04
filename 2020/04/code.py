entries = [x.replace("\n", " ") for x in open("input.txt").read().strip().split("\n\n")]

def validateByr(text):
	date = int(text)
	return len(text) == 4 and date >= 1920 and date <= 2002
	
def validateIyr(text):
	date = int(text)
	return len(text) == 4 and date >= 2010 and date <= 2020

def validateEyr(text):
	date = int(text)
	return len(text) == 4 and date >= 2020 and date <= 2030

def validateHgt(text):
	if len(text) < 3:
		return False
	units = text[-2:]
	num = int(text[:-2])
	return (units == "cm" and num >= 150 and num <= 193) or (units == "in" and num >= 59 and num <= 76)

def validateHcl(text):
	start = text[0:1]
	colour = text[1:]
	for c in colour:
		c = ord(c)
		if not ((c >= ord('0') and c <= ord('9')) or (c >= ord('a') and c <= ord('f'))):
			return False
	return start == "#" and len(colour) == 6

def validateEcl(text):
	return text in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def validatePid(text):
	try:
		return len(text) == 9 and int(text) != None
	except:
		return False

expected = [
	("byr", validateByr), 
	("iyr", validateIyr), 
	("eyr", validateEyr), 
	("hgt", validateHgt), 
	("hcl", validateHcl), 
	("ecl", validateEcl), 
	("pid", validatePid),
	#"cid",
]

def isValidEntry(entry, validate = False):
	fields = entry.split(" ")
	for (expect, validator) in expected:
		expect = expect + ":"
		found = False
		for field in fields:
			if expect in field:
				if (not validate) or validator(field[len(expect):]):
					found = True
					break
					
		if not found:
			return False
	return True


def task1(entries):
	valid = 0
	for entry in entries:
		if isValidEntry(entry):
			valid += 1
	return valid


def task2(entries):
	valid = 0
	for entry in entries:
		if isValidEntry(entry, True):
			valid += 1
	return valid
	


print("Task1:", task1(entries))
print("Task2:", task2(entries))

			
	
