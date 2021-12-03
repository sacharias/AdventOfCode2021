# f = open("input.txt", "r")
# data = f.read()
# data = data.split("\n")[:-1]

# print(data[0])

# total_len = len(data[0])

# gamma = ""

# for i in range(0, total_len):
#     zeros = 0
#     ones = 0
#     for j in range(0, len(data)):
#         val = int(data[j][i])
#         print(val)
#         if val == 1:
#             ones += 1
#         else:
#             zeros += 1

#     if ones > zeros:
#         gamma += "0"
#     else:
#         gamma += "1"

# print(gamma)

# print(3905 * 190)


# # 190



f = open("input.txt", "r")
data = f.read()
data = data.split("\n")[:-1]

oxygen = 0

total_len = len(data[0])

while True:
    for i in range(0, total_len):
        print("len", len(data))
        if len(data) <= 2:
            print(data)
            quit()

        zeros = 0
        ones = 0

        for j in range(0, len(data)):
            # print("hello", j, data[j])
            # print("he", data)
            val = int(data[j][i])
            if val == 1:
                ones += 1
            else:
                zeros += 1

        # filter step
        if ones < zeros:
            filtered_data = []
            for j in range(0, len(data)):
                val = int(data[j][i])
                if val == 1:
                    filtered_data.append(data[j])
        else:
            filtered_data = []
            for j in range(0, len(data)):
                val = int(data[j][i])
                if val == 0:
                    filtered_data.append(data[j])

        if len(filtered_data) <= 1:
            print("done")
            break

        print(type(filtered_data))
        data = filtered_data         

# oxygen 000100011010   282
# other 110010000101        3205

# 


# gamma = ""

# for i in range(0, total_len):
#     zeros = 0
#     ones = 0
#     for j in range(0, len(data)):
#         val = int(data[j][i])
#         print(val)
#         if val == 1:
#             ones += 1
#         else:
#             zeros += 1

#     if ones > zeros:
#         gamma += "0"
#     else:
#         gamma += "1"
