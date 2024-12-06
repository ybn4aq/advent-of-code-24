import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path1 = os.path.join(current_dir, "test_input1.txt")
file_path2 = os.path.join(current_dir, "test_input2.txt")
f1 = open(file_path1, "r")
f2 = open(file_path2, "r")
init1 = f1.readlines()
init2 = f2.readlines()
input1 = []
for i in init1:
    input1.append(i.split()[0])
# print(input1)
page_numbers = []
for i in init2:
    page_numbers.append(i.split()[0])
# print(page_numbers)
"""
Need to make dictionary of {rule: [prereq rules]}
"""
order = {}
for i in input1:
    line = i.split("|")
    # line[0] must be printed before line[1]
    rule, prereq = int(line[0]), int(line[1])
    if rule not in order:
        order[rule] = [prereq]
    else:
        order[rule].append(prereq)
print(order)
print(page_numbers)
valid_rules = []
# Check valid rules
for i in page_numbers:
    cur_rule = i.split(",")
    printed = set()
    valid = True
    for j in cur_rule:
        page = int(j)
    if valid:
        valid_rules.append(cur_rule)


# Add up middle values of valid rules




print(valid_rules)