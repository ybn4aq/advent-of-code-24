import os
import re


current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "test_input.txt")
f = open(file_path, "r")
raw = f.readlines()
puzzle = []
for line in raw:
    puzzle.append(line.split()[0])
print(puzzle)
"""
Could implement a graph?
Otherwise could scan through each horizontal, vertical, diagonal, and all of those backwards, looking for exact "XMAS" matches
Thefore, look for "XMAS" or "SMAX" in each row, column, and diagonal
Could use RegEx to find pattern matches
"""
pattern = "XMAS|SAMX"
ret = 0  # return
length = len(puzzle)
# ROWS
for row in puzzle:
    matches = re.findall(pattern, row)
    ret += len(matches)
# COLS
for i in range(length):
    col = ""
    for j in range(length):
        col += puzzle[j][i]
    matches = re.findall(pattern, col)
    ret += len(matches)
# DIAGONALS
for k in range(length):
    pass


for i in range(length):
    diag = ""
    for j in range(i, length):
        diag += puzzle[j][j]
        print(j,j)
    print(diag)


print(ret)