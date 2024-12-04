def get_occurrences_map(nums: list) -> dict:
    ret = {}
    for i in nums:
        if i not in ret:
            ret[i] = 1
        else:
            ret[i] += 1
    return ret
f = open("test_input.txt", "r")
lines = f.readlines()
left_list = [0] * len(lines)
right_list = [0] * len(lines)
for i in range(len(lines)):
    line = lines[i]
    split = line.split()
    left_list[i] = int(split[0])
    right_list[i] = int(split[1])
right_occurrences = get_occurrences_map(right_list)
similarities = 0
for i in left_list:
    print(left_list[i] + "")
    similarities += left_list[i] * right_occurrences.get(i, 0)
print(similarities)