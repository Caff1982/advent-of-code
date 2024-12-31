from collections import defaultdict
from itertools import permutations


with open("inputs/input_day8.txt") as f:
    lines = f.read().splitlines()

n_rows = len(lines)
n_cols = len(lines[0])
coord_dict = defaultdict(list)
for i in range(n_rows):
    for j in range(n_cols):
        if lines[i][j] != ".":
            coord_dict[lines[i][j]].append((i, j))


def is_in_bounds(row, col):
    return (0 <= row < n_rows) and (0 <= col < n_cols)


p1_nodes = set()
p2_nodes = set()
for freq, coords in coord_dict.items():
    for a, b in permutations(coords, 2):
        row1, col1 = a
        row2, col2 = b
        d_row = row2 - row1
        d_col = col2 - col1
        if is_in_bounds(row1 - d_row, col1 - d_col):
            p1_nodes.add((row1 - d_row, col1 - d_col))
        if is_in_bounds(row2 + d_row, col2 + d_col):
            p1_nodes.add((row2 + d_row, col2 + d_col))
        
        i = 1
        while is_in_bounds(row1 + i*d_row, col1 + i*d_col):
            p2_nodes.add((row1 + i*d_row, col1 + i*d_col))
            i += 1
        i = 1
        while is_in_bounds(row2 - i*d_row, col2 - i*d_col):
            p2_nodes.add((row2 - i*d_row, col2 - i*d_col))
            i += 1

print(len(p1_nodes))
print(len(p2_nodes))