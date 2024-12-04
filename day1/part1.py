f = open("input.txt", "r")
lines = f.readlines()
left_list = [0] * len(lines)
right_list = [0] * len(lines)
for i in range(len(lines)):
    line = lines[i]
    split = line.split()
    left_list[i] = int(split[0])
    right_list[i] = int(split[1])
left_list.sort()
right_list.sort()
print(left_list)
print("====")
print(right_list)
distance = 0  # return
for i in range(len(lines)):
    distance += abs(left_list[i] - right_list[i])
print(distance)