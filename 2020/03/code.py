entries = [[(c == '#') for c in x] for x in open("input.txt").read().strip().split('\n')]

def isBlocked(x, y):
	row = entries[y]
	x = x % len(row)
	return row[x]

def treesForSlope(entries, right, down):
	x = 0
	y = 0
	trees = 0
	
	while y < len(entries):
		if isBlocked(x,y):
			trees += 1
		x += right
		y += down

	return trees

def task1(entries):
	return treesForSlope(entries, 3, 1)

def task2(entries):
	slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
	
	product = 1
	for (right, down) in slopes:
		product = product * treesForSlope(entries, right, down)
	
	return product

print("Task1:", task1(entries))
print("Task2:", task2(entries))
