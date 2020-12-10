adapters = [int(x) for x in open("input.txt", "r").read().strip().split("\n")]
adapters.sort()

adapters.insert(0, 0) # first "adapter" is the 0 jolt supply
adapters.append(adapters[len(adapters) - 1] + 3) # my adapter is +3 final one

def task1(adapters):
	oneVolt = 0
	threeVolt = 0
	
	i = 1
	while i < len(adapters):
		adapter = adapters[i]
		prev = adapters[i - 1]
		
		diff = adapter - prev
		if diff == 1:
			oneVolt += 1
		elif diff == 3:
			threeVolt += 1
		
		i += 1
	
	return oneVolt * threeVolt

print(task1(adapters))
