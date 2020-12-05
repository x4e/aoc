
#entries = open("input.txt", "r").read().strip().split('\n')
entries = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]

rows = 127
cols = 7

passes = []

for entry in entries:
	prevRow = rows
	row = rows // 2
	prevCol = cols
	col = cols // 2
	
	for c in entry:
		if c == 'F':
			nPrev = row
			row = row - round((prevRow - row) / 2)
			prevRow = nPrev
		elif c == 'B':
			nPrev = row
			row = row + round((prevRow - row) / 2)
		elif c == 'L':
			nPrev = col
			col = col - round((prevCol - col) / 2)
			prevCol = nPrev
		elif c == 'R':
			nPrev = col
			col = col + round((prevCol - col) / 2)
			prevCol = nPrev
	
	seatId = (row * 8) + col
	passes.append((row, col, seatId))
	
	print(entry, row, col, seatId)


def task1(passes):
	highest = 0
	for (row, col, seatId) in passes:
		if seatId > highest:
			highest = seatId
	return highest

print("Task1:", task1(passes))

