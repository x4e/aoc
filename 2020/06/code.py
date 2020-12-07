entries = [x.split("\n") for x in open("input.txt").read().strip().split("\n\n")]

def task1(entries):
	total = 0
	for entry in entries:
		group = set()
		for person in entry:
			for question in person:
				group.add(question)
		total += len(group)
	return total


def task2(entries):
	def list_and(first, second):
		out = set()
		for a in first:
			if a in second:
				out.add(a)
		for b in second:
			if b in first:
				out.add(b)
		return out
	
	alphabet = [chr(x) for x in range(ord('a'), ord('z') + 1)]
	
	total = 0
	for entry in entries:
		everyone = set(alphabet)
		for person in entry:
			answered = set()
			for question in person:
					answered.add(question)
			everyone = list_and(everyone, answered)
		total += len(everyone)
	return total


print("Task1:", task1(entries))
print("Task2:", task2(entries))
