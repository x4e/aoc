lines = open("input.txt", "r").read().strip().split("\n")

operators = ["+", "*"]

class TokenBuffer():
	def __init__(self, string, index = 0):
		self.string = string
		self.i = index
		self.whitespace()
	
	def whitespace(self):
		while self and self.string[self.i].isspace():
			self.i += 1
	
	def token(self):
		out = ""
		next = self.peek()
		if next.isnumeric() or next in operators or next == "(" or next == ")":
			out = self.char()
		self.whitespace()
		return out
	
	def char(self):
		out = self.string[self.i]
		self.i += 1
		return out
	
	def peek(self):
		return self.string[self.i]
	
	def __len__(self):
		return len(self.string) - self.i

# credit to my bro dijkstra
def parse(buf, ignorePrecedence = True):
	def higherPrecedence(op, op2):
		return op == "+" and op2 == "*"
	
	def applyOp(op, lhs, rhs):
		lhs = int(lhs)
		rhs = int(rhs)
		out = 0
		if op == "+":
			out = lhs + rhs
		elif op == "*":
			out = lhs * rhs
		else:
			raise Exception("Unknown operator (" + op + ")")
		return str(out)
	
	outputQ = []
	opStack = []
	while buf:
		token = buf.token()
		if token.isnumeric():
			outputQ.append(token)
		elif token in operators:
			while opStack:
				c = opStack[-1]
				if c != "(" and c != ")" and (ignorePrecedence or higherPrecedence(c, token)):
					op = opStack.pop()
					rhs = outputQ.pop()
					lhs = outputQ.pop()
					outputQ.append(applyOp(op, lhs, rhs))
				else:
					break
			opStack.append(token)
		elif token == "(":
			opStack.append(token)
		elif token == ")":
			while opStack and opStack[-1] != "(":
				op = opStack.pop()
				rhs = outputQ.pop()
				lhs = outputQ.pop()
				outputQ.append(applyOp(op, lhs, rhs))
			opStack.pop()
	while opStack:
		op = opStack.pop()
		rhs = outputQ.pop()
		lhs = outputQ.pop()
		outputQ.append(applyOp(op, lhs, rhs))
	return int(outputQ[0])

def task1(lines):
	sum = 0
	for line in lines:
		buf = TokenBuffer(line)
		sum += parse(buf)
	return sum

def task2(lines):
	sum = 0
	for line in lines:
		buf = TokenBuffer(line)
		sum += parse(buf, False)
	return sum

print("Task1:", task1(lines))
print("Task2:", task2(lines))
