from math import floor, ceil

entries = open("input.txt", "r").read().strip().split('\n')
#entries = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]

rows = 127
cols = 7

passes = []

for entry in entries:
	rowMax = rows
	rowMin = 0
	row = 0
	colMax = cols
	colMin = 0
	col = 0
	
	for c in entry:
		if c == 'F':
			rowMax -= ((rowMax - rowMin) // 2) + 1
			row = rowMin
		elif c == 'B':
			rowMin += ((rowMax - rowMin) // 2) + 1
			row = rowMax
		elif c == 'L':
			colMax -= ((colMax - colMin) // 2) + 1
			col = colMin
		elif c == 'R':
			colMin += ((colMax - colMin) // 2) + 1
			col = colMax
	
	seatId = (row * 8) + col
	passes.append((row, col, seatId))


def task1(passes):
	highest = 0
	for (row, col, seatId) in passes:
		if seatId > highest:
			highest = seatId
	return highest

def task2(passes):
	ids = set()
	for (row, col, seatId) in passes:
		ids.add(seatId)
	for id in ids:
		if id + 1 not in ids:
			if id + 2 in ids:
				return id + 1
		elif id - 1 not in ids:
			if id - 2 in ids:
				return id - 1

print("Task1:", task1(passes))
print("Task2:", task2(passes))

