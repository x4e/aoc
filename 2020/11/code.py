import copy

lines = open("input.txt", "r").read().strip().split("\n")

seats = [] # 0 = floor, 1 = empty seat, 2 = occupied seat
for line in lines:
	row = []
	seats.append(row)
	for c in line:
		if c == '.':
			row.append(0)
		elif c == 'L':
			row.append(1)
		elif c == '#':
			row.append(2)

def getSeat(seats, x, y):
	if x < 0 or y < 0 or y >= len(seats) or x >= len(seats[y]):
		return -1
	else:
		return seats[y][x]

def isOccupied(seats, x, y):
	return getSeat(seats, x, y) == 2

# count num occupied adjacent seats
def numAdjacent(seats, x, y):
	occupied = 0
	for dx in range(-1, 2):
		for dy in range(-1, 2):
			if (dx != 0 or dy != 0) and isOccupied(seats, x + dx, y + dy):
				occupied += 1
	return occupied

def visibleAdjacent(seats, x, y):
	def firstVisible(seats, x, y, dx, dy):
		seat = 0
		while seat == 0:
			x += dx
			y += dy
			seat = getSeat(seats, x, y)
		return seat
	
	occupied = 0
	for dx in range(-1, 2):
		for dy in range(-1, 2):
			if (dx != 0 or dy != 0) and firstVisible(seats, x, y, dx, dy) == 2:
				occupied += 1
	return occupied

def printSeats(seats):
	print("---")
	for row in seats:
		out = ""
		for seat in row:
			if seat == 0:
				out += "."
			elif seat == 1:
				out += "L"
			elif seat == 2:
				out += "#"
		print(out)

def simulateRun(seats, visible = False, occupiedLimit = 4):
	newSeats = copy.deepcopy(seats)
	
	counter = numAdjacent
	if visible:
		counter = visibleAdjacent
	
	changed = 0
	y = 0
	while y < len(seats):
		row = seats[y]
		x = 0
		while x < len(row):
			seat = getSeat(seats, x, y)
			adjacent = counter(seats, x, y)
			if seat == 1 and adjacent == 0: # empty
				newSeats[y][x] = 2 # occupied
				changed += 1
			elif seat == 2 and adjacent >= occupiedLimit: # occupied
				newSeats[y][x] = 1 # empty
				changed += 1
			x += 1
		y += 1
	
	return (newSeats, changed)

def task1(seats):
	changed = 1
	while changed > 0:
		(seats, changed) = simulateRun(seats)
	
	# count occupied seats
	occupied = 0
	y = 0
	while y < len(seats):
		row = seats[y]
		x = 0
		while x < len(row):
			seat = getSeat(seats, x, y)
			if seat == 2: # occupied
				occupied += 1
			x += 1
		y += 1
	return occupied

def task2(seats):
	changed = 1
	while changed > 0:
		(seats, changed) = simulateRun(seats, True, 5)
	
	# count occupied seats
	occupied = 0
	y = 0
	while y < len(seats):
		row = seats[y]
		x = 0
		while x < len(row):
			seat = getSeat(seats, x, y)
			if seat == 2: # occupied
				occupied += 1
			x += 1
		y += 1
	return occupied

print("Task1:", task1(seats))
print("Task2:", task2(seats))
