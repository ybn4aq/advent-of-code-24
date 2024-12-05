import os

def damp(line: list[int]) -> bool:
    l, r = 0, 1
    mode = ""
    while r < len(line):
        left, right = line[l], line[r]
        if abs(right - left) > 3 or right == left:
            return False
        if mode == "":
            if right > left:
                mode = "inc"
            else:  # right < left
                mode = "dec"
        elif mode == "inc":
            if right < left:
                return False
        else:  # mode = "dec"
            if right > left:
                return False
        l += 1
        r += 1
    return True
    


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
"""
Brute force
"""
for line in nums:
    valid = False
    if not damp(line):
        for skip in range(len(line)):
            new_line = line.copy()
            new_line.pop(skip)
            if damp(new_line):
                valid = True
                break
    else:
        valid = True
    if valid:
        safe += 1
print(safe)