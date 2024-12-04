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