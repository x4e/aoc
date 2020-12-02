import re

regex = r'([0-9]+)-([0-9]+) ([A-z0-9]): (.*)'
entries = open("input.txt").read().strip().split('\n')

def task1(entries):
	valid = 0
	
	for entry in entries:
		(min, max, char, password) = re.findall(regex, entry)[0]
		min = int(min)
		max = int(max)
		char = char[0]
		found = 0

		for c in password:
			if c == char:
				found += 1

		if found >= min and found <= max:
			valid += 1
	
	return valid

def task2(entries):
	valid = 0

	for entry in entries:
		(min, max, char, password) = re.findall(regex, entry)[0]
		min = int(min) - 1
		max = int(max) - 1
		char = char[0]

		if len(password) > max and ((password[min] == char) != (password[max] == char)):
			valid += 1
	
	return valid

print("Task1:", task1(entries))
print("Task2:", task2(entries))
