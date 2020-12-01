import sys

desiredSum = 2020

entries = [int(i) for i in open("input.txt").read().strip().split()]

for e1 in entries:
	for e2 in entries:
		for e3 in entries:
			if e1 + e2 + e3 == desiredSum:
				print(e1, "*", e2, "*", e3, "=", e1 * e2 * e3)
				sys.exit()

print("Bad input")
