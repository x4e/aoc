lines = open("input.txt", "r").read().strip().split("\n")

rules = {}

i = 0
while i < len(lines):
	line = lines[i]
	if not line:
		break
	else:
		split = line.split(": ")
		name = split[0]
		ranges = [[int(y) for y in x.split("-")] for x in split[1].split(" or ")]
		rules[name] = ranges
	i += 1

i += 2
myTicket = [int(x) for x in lines[i].split(",")]
i += 3

nearby = []
while i < len(lines):
	line = lines[i]
	if not line:
		break
	else:
		nearby.append([int(x) for x in line.split(",")])
	i += 1

def validateRule(num, ranges):
	for range in ranges:
		if num >= range[0] and num <= range[1]:
			return True
	return False

def task1(rules, nearby):
	scanErrorRate = 0
	for ticket in nearby:
		for value in ticket:
			valid = False
			for (name, ranges) in rules.items():
				if validateRule(value, ranges):
					valid = True
					break
			if not valid:
				scanErrorRate += value
	return scanErrorRate

def task2(rules, nearby, myTicket):
	# First collect all the valid tickets
	validTickets = []
	for ticket in nearby:
		validTicket = True
		for value in ticket:
			valid = False
			for (name, ranges) in rules.items():
				if validateRule(value, ranges):
					valid = True
					break
			if not valid:
				validTicket = False
				break
		if validTicket:
			validTickets.append(ticket)
	
	# Count the number of fields in a ticket
	numFields = len(nearby[0])
	fields = list(range(numFields))
	
	# Each rule could be any field index
	posPositions = {}
	for (name, ranges) in rules.items():
		posPositions[name] = fields.copy()
	
	# If any field index does not match a given rule, remove that index from the rules possible indexes
	for ticket in validTickets:
		i = 0
		for value in ticket:
			valid = False
			for (name, ranges) in rules.items():
				if not validateRule(value, ranges):
					posPositions[name].remove(i)
			i += 1
	
	# Some rules will have multiple possible indexes
	# However some rules will only have one
	# If any rule only has one index we know that index belongs to that rule
	# And we also therefore know it doesnt belong to any other rule so we can remove it from every other rules possible indexes
	# Continue this until every rule has a known certain index
	positions = {}
	while len(posPositions) > 0:
		for (name, poses) in posPositions.items():
			if len(poses) == 1:
				index = poses[0]
				positions[name] = index
				posPositions.pop(name)
				
				for (name, poses) in posPositions.items():
					poses.remove(index)
				
				break
	
	# Find the product of all the departure fields on my ticket
	product = 1
	for (name, index) in positions.items():
		if name[:9] == "departure":
			product *= myTicket[index]
	
	return product
	

print("Task1:", task1(rules, nearby))
print("Task2:", task2(rules, nearby, myTicket))
