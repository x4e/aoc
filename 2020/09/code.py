class CircularStack():
	def __init__(self, size):
		self.size = size
		self.inner = [None] * size
		self.head = 0
	
	def push(self, item):
		self.inner[self.head % self.size] = item
		self.head += 1
	
	def pop(self):
		self.head -= 1
		return self.inner[self.head % self.size]
	
	def __iter__(self):
		i = 0
		top = self.size
		if self.head < self.size:
			top = self.head
		while i < top:
			yield self.inner[i]
			i += 1

numbers = [int(x) for x in open("input.txt", "r").read().strip().split("\n")]

def task1(numbers):
	size = 25
	stack = CircularStack(size)
	
	def addsTo(stack, num):
		for item in stack:
			for item2 in stack:
				if item + item2 == num:
					return True
		return False
	
	for num in numbers:
		if stack.head >= size:
			if not addsTo(stack, num):
				return num
		stack.push(num)

def task2(numbers, invalid):
	i = 0
	while i < len(numbers):
		i2 = i
		sum = 0
		low = -1
		high = -1
		
		while i2 >= 0:
			num = numbers[i2]
			sum += num
			if low == -1 or num < low:
				low = num
			if high == -1 or num > high:
				high = num
			
			if sum == invalid:
				return low + high
			elif sum > invalid:
				break
			
			i2 -= 1
		
		i += 1
			
invalid = task1(numbers)
print("Task1:", invalid)
print("Task2:", task2(numbers, invalid))
