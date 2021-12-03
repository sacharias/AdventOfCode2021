
f = open("input.txt", "r")
data = f.read()
data = data.split("\n")[:-1]

depth = 0
forward = 0
aim = 0

for row in data:
    values = row.split(" ")
    instr = values[0]
    amount = int(values[1])

    if instr == "forward":
        forward += amount
        depth += (aim * amount)
    elif instr == "down":
        # depth += amount
        aim += amount
    elif instr == "up":
        # depth -= amount
        aim -= amount

print(depth, forward, depth * forward)
# print(data)