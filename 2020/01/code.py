import sys

desiredSum = 2020

entries = [int(i) for i in open("input.txt").read().strip().split()]

def task1(entries):
	for e1 in entries:
		for e2 in entries:
			if e1 + e2 == desiredSum:
				return e1 * e2
	print("Failed to solve")
	sys.exit(1)

def task2(entries):
	for e1 in entries:
		for e2 in entries:
			for e3 in entries:
				if e1 + e2 + e3 == desiredSum:
					return e1 * e2 * e3
	print("Failed to solve")
	sys.exit(1)


print("Task1:", task1(entries))
print("Task2:", task2(entries))
