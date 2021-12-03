f = open("input2.txt", "r")

# f = open("inputextra.txt", "r")

data = f.read()
data = list(map(int, data.split("\n")))


# print(data)

# Part 1
counter = 0
for i in range(1, len(data)):
    val1 = data[i-1]
    val2 = data[i]

    if val2 > val1:
        counter += 1

# print(counter)
prev_sum = -1

counter = 0
for i in range(0, len(data) - 2):
    sum = data[i] + data[i+1] + data[i+2]
    if prev_sum == -1:
        prev_sum = sum
        continue

    if sum > prev_sum:
        counter += 1
    
    prev_sum = sum

print(counter)

