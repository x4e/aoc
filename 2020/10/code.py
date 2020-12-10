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

def task2(adapters):
	paths = {}
	
	paths[0] = 1 # supply
	i = 1
	while i < len(adapters):
		adapter = adapters[i]
		
		routes = 0
		i2 = i - 1
		while i2 >= 0:
			adap2 = adapters[i2]
			diff = adapter - adap2
			if diff > 3:
				break
			else:
				routes += paths[i2]
			i2 -= 1
		paths[i] = routes
		
		i += 1
	
	return paths[len(adapters) - 1]

print(task1(adapters))
print(task2(adapters))
