# Coordinates are tuples (x, y, z, w)
# If a coordinate is in the set then the cube at that coordinate is active
grid = set()

def get(grid, pos):
	return pos in grid

def set(grid, pos, active):
	if active:
		grid.add(pos)
	elif pos in grid:
		grid.remove(pos)

def allNeighbours(grid, pos, hyperDimension = False):
	(x,y,z,w) = pos
	for dx in range(-1,2):
		for dy in range(-1,2):
			for dz in range(-1,2):
				# Do we include the fourth hypercube dimension? Otherwise assume dw = 0
				if hyperDimension:
					for dw in range(-1, 2):
						# check they don't all equal 0, which would lead to the original coordinate being produced
						if dx != 0 or dy != 0 or dz != 0 or dw != 0:
							yield (x + dx, y + dy, z + dz, w + dw)
				else:
					if dx != 0 or dy != 0 or dz != 0:
						yield (x + dx, y + dy, z + dz, w)

def cycle(grid, hyperDimension = False):
	# Each neighbour of any active grid, and the number of active grids that it neighbours
	neighbours = {}
	
	# For every active position, let all its neighbours know they have one more active neighbour
	for pos in grid:
		if pos not in neighbours:
			neighbours[pos] = 0
		for neighbour in allNeighbours(grid, pos, hyperDimension):
			if neighbour in neighbours:
				neighbours[neighbour] += 1
			else:
				neighbours[neighbour] = 1
	
	for (pos, numNeighs) in neighbours.items():
		if get(grid, pos):
			if not (numNeighs == 2 or numNeighs == 3):
				set(grid, pos, False)
		else:
			if numNeighs == 3:
				set(grid, pos, True)

# parse input
y = 0
for line in open("input.txt", "r").read().strip().split("\n"):
	x = 0
	for c in line:
		active = (c == "#")
		set(grid, (x, y, 0, 0), active)
		x += 1
	y += 1


def task1(grid):
	for i in range(0, 6):
		cycle(grid)
	return len(grid)

def task2(grid):
	for i in range(0, 6):
		cycle(grid, True)
	return len(grid)


print("Task1:", task1(grid.copy()))		
print("Task2:", task2(grid.copy()))			
	