input = open("input.txt", "r").read().strip().split(",")

def findNth(input, nth):
	prev = 0
	prevStore = 0
	numbers = {}
	i = 0
	while i < len(input):
		num = int(input[i])
		prev = num
		if num in numbers:
			prevStore = numbers[num]
		else:
			prevStore = None
		numbers[num] = i
		i += 1
	
	while i < nth:
		num = 0
		if prevStore != None:
			prevDif = i - 1 - prevStore
			num = prevDif
		else:
			prevStore = 0
			num = 0
		
		if num in numbers:
			prevStore = numbers[num]
		else:
			prevStore = None
		
		numbers[num] = i
		prev = num
		
		i += 1
	
	return prev

def task1(input):
	return findNth(input, 2020)

def task2(input):
	return findNth(input, 30000000)

print("Task1:", task1(input))
print("Task2:", task2(input))
