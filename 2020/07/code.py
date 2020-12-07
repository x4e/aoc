entries = open("input.txt", "r").read().strip().split("\n")

# key = name: string
# value = dict: key = bagname: string, value = num: int
bags = {}

# create a tree like structure of bags to their potential contents
for entry in entries:
	containFirst = entry.find(" bags contain ")
	bagname = entry[:containFirst]
	contents = entry[containFirst + len(" bags contain "):-1].split(", ") # -1 to remove trailing fullstop
	
	innerBags = {}
	for content in contents:
		if content[-1:] == "s": # end with bag or bags?
			content = content[:-len(" bags")]
		else:
			content = content[:-len(" bag")]
		if content != "no other":
			amount = int(content[:1]) # assume 1 digit number
			innerbagname = content[2:] # +1 for space
			innerBags[innerbagname] = amount
	
	bags[bagname] = innerBags

def task1(bags):
	myBag = "shiny gold"
	
	def findBagsThatContain(bags, target):
		contain = set()
		
		for (bagname, children) in bags.items():
			for (child, num) in children.items():
				if num > 0 and child == target:
					contain.add(bagname)
		
		return contain
	
	rootBags = set()
	
	# this could get infinite lol
	contain = findBagsThatContain(bags, myBag)
	while len(contain) > 0:
		bag = contain.pop()
		rootBags.add(bag)
		contain = contain | findBagsThatContain(bags, bag)
	
	return len(rootBags)

def task2(bags):
	myBag = "shiny gold"
	
	totalChildBags = 0
	findChildrenOf = {myBag: 1}
	while len(findChildrenOf) > 0:
		(bag, parentNum) = findChildrenOf.popitem()
		for (child, num) in bags[bag].items():
			totalChildBags += num * parentNum
			findChildrenOf[child] = num * parentNum
	
	return totalChildBags # thats a lotta bags lol


print("Task1:", task1(bags))
print("Task2:", task2(bags))
