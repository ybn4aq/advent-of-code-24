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
"""
May necessitate a two pointer approach. 
Brute Force: Could do an initial scan to see if line is safe without any alterations, and then try and do alterations
    Could attempt each line with every number removed
Is it guaranteed that if the first removal doesn't work, that the line is unsafe no matter what?
Potential issue: If we try to damp at the very start, do we know that inc vs dec mode is accurate?
Could be helpful to make each line a linked list, would make handling damps way easier
Could try always removing left? - Issue could attempt to Damp when l = 0
Right bias: 554
Left bias: 533
"""
for line in nums:
    l, r = 0, 1
    mode = ""
    damp = False  # will be true if we damp
    valid = True
    if line == []:
        print("Debug!")
    while r < len(line):
        left, right = line[l], line[r]
        if abs(right - left) > 3 or right == left:
            if damp:
                valid = False
                break
            else:
                if mode == "inc":
                    # Inc Damp
                    damp = True
                    l -= 1
                    if l < 0:
                        # TODO
                        l += 2
                        r += 1
                        right = line[r]
                    left = line[l]
                    if right > left and abs(right - left) <= 3:
                        # Successful Damp
                        l += 1
                    else:
                        # Failed Damp
                        valid = False
                        break
                elif mode == "dec":
                    # Dec Damp
                    damp = True
                    l -= 1
                    if l < 0:
                        # TODO
                        l += 2
                        r += 1
                        right = line[r]
                    left = line [l]
                    if right < left and abs(right - left) <= 3:
                        # Successful Damp
                        l += 1
                    else:
                        # Failed Damp
                        valid = False
                        break
                else:
                    # Ambiguous Damp
                    damp = True
                    l -= 1
                    if l < 0:
                        # TODO
                        l += 2
                        r += 1
                        right = line[r]
                    left = line[l]
                    if abs(right - left) > 3:
                        # Failed Damp
                        valid = False
                        break
                    if right > left:
                        # Successful Damp
                        mode = "inc"
                        l += 1
                    elif right < left:
                        # Successful Damp
                        mode = "dec"
                        l += 1
                    else:  # right == left
                        # Failed Damp
                        valid = False
                        break
        if mode == "":
            if right > left:
                mode = "inc"
            elif right < left:
                mode = "dec"
        elif mode == "inc":
            if right <= left:
                if damp:
                    valid = False
                    break
                else:
                    # Inc Damp
                    damp = True
                    l -= 1
                    if l < 0:
                        # TODO
                        l += 2
                        r += 1
                        right = line[r]
                    left = line[l]
                    if right > left and abs(right - left) <= 3:
                        # Successful Damp
                        l += 1
                    else:
                        # Failed Damp
                        valid = False
                        break
        else:  # mode == "dec"
            if right >= left:
                if damp:
                    valid = False
                    break
                else:
                    # Dec Damp
                    damp = True
                    l -= 1
                    if l < 0:
                        # TODO
                        l += 2
                        r += 1
                        right = line[r]
                    left = line[l]
                    if right < left and abs(right - left) <= 3:
                        # Successful Damp
                        l += 1
                    else:
                        # Failed Damp
                        valid = False
                        break
        l += 1
        r += 1
    if valid:
        safe += 1
    else:
        print(line)
print(safe)
