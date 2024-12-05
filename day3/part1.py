import os
import re

def mul(x,y):
    return x * y

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "input.txt")
f = open(file_path, "r").readlines()
memory = ""
for i in f:
    memory += str(i)
"""
RegEx approach seems appropriate here
Capture all valid mul calls and add them together
"""
pattern = "mul\(\d+,\d+\)"
matches = re.findall(pattern, memory)
ret = 0  # return
for match in matches:
    ret += eval(match)


print(ret)