from math import pow

lines = open("input.txt", "r").read().strip().split("\n")

def task1(lines):
	andMask = 0
	orMask = 0
	mem = {}
	
	for line in lines:
		start = line[:4]
		if start == "mask":
			andMask = 0b111111111111111111111111111111111111
			orMask = 0b000000000000000000000000000000000000
			mask = line[7:]
			andMask &= int(mask.replace("X", "1"), 2)
			orMask |= int(mask.replace("X", "0"), 2)
		elif start == "mem[":
			num = ""
			for c in line[4:]:
				try:
					int(c)
					num += c
				except:
					break
			numLen = len(num)
			num = int(num)
			val = int(line[4 + numLen + 4:])
			val &= andMask
			val |= orMask
			mem[num] = val
	
	sum = 0
	for (index, item) in mem.items():
		sum += item
	return sum

def task2(lines):
	orMask = 0
	floatingMask = set()
	mem = {}
	
	for line in lines:
		start = line[:4]
		if start == "mask":
			orMask = 0b000000000000000000000000000000000000
			mask = line[7:]
			orMask |= int(mask.replace("X", "0"), 2)
			
			floatingMask = set()
			i = 0
			while i < len(mask):
				if mask[i] == "X":
					floatingMask.add(i)
				i += 1
			
		elif start == "mem[":
			addr = ""
			for c in line[4:]:
				try:
					int(c)
					addr += c
				except:
					break
			addrLen = len(addr)
			addr = int(addr)
			val = int(line[4 + addrLen + 4:])
			addr |= orMask
s			numXs = len(floatingMask)
			for num in range(int(pow(2, numXs))):
				numStr = bin(num)[2:].rjust(38, "0")
				addrStr = bin(addr)[2:].rjust(38, "0")
				
				numI = len(numStr) - 1
				newAddr = ""
				for i in range(0, 36):
					if i in floatingMask:
						newAddr += numStr[numI]
						numI -= 1
					else:
						newAddr += addrStr[i]
				
				mem[int(newAddr, 2)] = val
	
	sum = 0
	for (index, item) in mem.items():
		sum += item
	return sum

print(task1(lines))
print(task2(lines))
