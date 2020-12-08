class VmState():
	def __init__(self):
		self.ip = 0
		self.acl = 0
	
	def __str__(self):
		return "ip: {}, acl: {}".format(self.ip, self.acl)

def interpret(code, debugger = lambda code, state: True):
	state = VmState()
	
	while state.ip < len(code):
		(opcode, operand) = code[state.ip]
		
		if not debugger(code, state):
			break # early terminate
		
		if opcode == "nop":
			pass
		elif opcode == "acc":
			state.acl += operand
		elif opcode == "jmp":
			state.ip += operand - 1 # -1 to account for the +1 that will occur at the end of instruction interpretation
		
		state.ip += 1
	
	return state

def task1(code):
	acl = 0
	encountered = set()
	def debugger(code, state):
		nonlocal acl
		if state.ip in encountered:
			acl = state.acl
			return False
		encountered.add(state.ip)
		return True
	
	interpret(code, debugger)
	return acl

def task2(code):
	def test(code): # tests if the code loops, if it doesnt returns the state after program termination
		loops = False
		
		encountered = set()
		def debugger(code, state):
			nonlocal loops
			if state.ip in encountered:
				# we encountered this instruction before
				loops = True
				return False
			encountered.add(state.ip)
			return True
		
		state = interpret(code, debugger)
		if loops:
			return None
		else:
			return state
	
	# For each instruction, if it is a jmp/nop test if switching it would fix the infinite loop
	i = 0
	while i < len(code):
		(opcode, operand) = code[i]
		if opcode == "jmp":
			code[i] = ("nop", operand)
			out = test(code)
			if out != None:
				return out.acl
			code[i] = ("jmp", operand)
		elif opcode == "nop":
			code[i] = ("jmp", operand)
			out = test(code)
			if out != None:
				return out.acl
			code[i] = ("nop", operand)
		i += 1
	

code = [(x[0], int(x[1])) for x in [(x.split(" ")) for x in open("input.txt", "r").read().strip().split("\n")]]

print("Task1:", task1(code))
print("Task2:", task2(code))
