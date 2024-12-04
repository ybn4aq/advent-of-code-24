import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "input.txt")
f = open(file_path, "r")
init = f.readlines()
lines = []
for i in init:
    lines.append(i.split())
nums = []  # not a very efficient way of doing this but w/e
for i in lines:
    nums.append([int(x) for x in i])
safe = 0  # ret
for line in nums:
    last_num = line[0]
    mode = ""
    valid = True
    for i in range(1, len(line)):
        cur_num = line[i]
        if abs(cur_num - last_num) > 3 or cur_num == last_num:
            valid = False
            break
        if mode == "":
            if cur_num > last_num:
                mode = "inc"
            elif cur_num < last_num:
                mode = "dec"
        elif mode == "inc":
            if cur_num < last_num:
                valid = False
                break
        else:  # mode == "dec":
            if cur_num > last_num:
                valid = False
                break
        last_num = cur_num
    if valid:
        safe += 1  # if we are at this point, we have identified a safe line
print(safe)
