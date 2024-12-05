import os
import re

# Used ChatGPT to help with RegEx--needed to use escape character for () and '

def mul(x,y):
    return x * y

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "input.txt")
f = open(file_path, "r").readlines()
memory = ""
for i in f:
    memory += str(i)
pattern = "mul\(\d+,\d+\)|do\(\)|don\'t\(\)"
matches = re.findall(pattern, memory)
ret = 0  # return
do = True
for i in matches:
    if i == "do()":
        do = True
    elif i == "don't()":
        do = False
    else:
        if do:
            ret += eval(i)
print(ret)
