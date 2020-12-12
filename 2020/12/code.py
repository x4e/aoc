from math import cos, sin, radians

instructions = [(x[:1], int(x[1:])) for x in open("input.txt", "r").read().strip().split("\n")]

class Entity():
	def __init__(self):
		self.x = 0
		self.y = 0
		self.rot = 90 # degs

def task1(instructions):
	ship = Entity()
	for (dir, amount) in instructions:
		if dir == "N":
			ship.y += amount
		elif dir == "S":
			ship.y -= amount
		elif dir == "E":
			ship.x += amount
		elif dir == "W":
			ship.x -= amount
		elif dir == "L":
			ship.rot -= amount
		elif dir == "R":
			ship.rot += amount
		elif dir == "F":
			ship.y += int(cos(radians(ship.rot)) * amount)
			ship.x += int(sin(radians(ship.rot)) * amount)
	
	return abs(ship.x) + abs(ship.y)

def task2(instructions):
	ship = Entity()
	waypoint = Entity()
	waypoint.x = 10
	waypoint.y = 1
	
	def rotatePoint(px, py, rot): # rot = counter clockwise
		rads = radians(rot)
		srad = sin(rads)
		crad = cos(rads)
		
		nx = crad * px - srad * py
		ny = srad * px + crad * py
		return (round(nx), round(ny))
	
	for (dir, amount) in instructions:
		if dir == "N":
			waypoint.y += amount
		elif dir == "S":
			waypoint.y -= amount
		elif dir == "E":
			waypoint.x += amount
		elif dir == "W":
			waypoint.x -= amount
		elif dir == "L":
			(nx, ny) = rotatePoint(waypoint.x, waypoint.y, amount)
			waypoint.x = nx
			waypoint.y = ny
		elif dir == "R":
			(nx, ny) = rotatePoint(waypoint.x, waypoint.y, -amount)
			waypoint.x = nx
			waypoint.y = ny
		elif dir == "F":
			ship.y += waypoint.y * amount
			ship.x += waypoint.x * amount
	
	return abs(ship.x) + abs(ship.y)

print("Task1:", task1(instructions))
print("Task2:", task2(instructions))
