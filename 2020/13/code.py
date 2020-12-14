input = open("input.txt", "r").read().strip().split("\n")
arrival = int(input[0])
buses = []
for bus in input[1].split(","):
	if bus != "x":
		buses.append(int(bus))
	else:
		buses.append(-1)

def task1(arrival, buses):
	time = arrival
	while True:
		for bus in buses:
			if bus != -1 and time % bus == 0:
				return bus * (time - arrival)
		time += 1

def task2(buses):
	time = 0
	step = 1
	i = 0
	while i < len(buses):
		bus = buses[i]
		if bus != -1:
			while (time + i) % bus != 0:
				time += step
			step *= bus
		i += 1
	return time

print("Task1:", task1(arrival, buses))
print("Task2:", task2(buses))
