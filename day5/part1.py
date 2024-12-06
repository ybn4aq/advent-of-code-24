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
page_numbers = []
for i in init2:
    page_numbers.append(i.split()[0])
# Need to make dictionary of {rule: [prereq rules]}
order = {}
for i in input1:
    line = i.split("|")
    # line[0] must be printed before line[1]
    rule, prereq = int(line[0]), int(line[1])
    if rule not in order:
        order[rule] = [prereq]
    else:
        order[rule].append(prereq)
valid_rules = []
# Check valid rules
# 75,97,47,61,53
# for i in line: if any of prereqs have been printed before, invalid
for i in page_numbers:
    cur_rule = i.split(",")
    printed = set()
    valid = True
    for j in cur_rule:
        page = int(j)
        if page in order:
            for prereq in order[page]:
                if prereq in printed:
                    valid = False
                    break
        printed.add(page)
    if valid:
        valid_rules.append(cur_rule)
print(valid_rules)

# Add up middle values of valid rules
ret = 0  # return
for i in valid_rules:
    n = len(i)
    mid = n // 2
    ret += int(i[mid])
print(ret)