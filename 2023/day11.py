from itertools import combinations


with open('inputs/input_day11.txt', 'r') as f:
    lines = f.read().splitlines()


# Get the row & column indices to expand
col_expansion = []
for i in range(len(lines[0])):
    if not any(row[i] == '#' for row in lines):
        col_expansion.append(i)
row_expansion = []
for i, line in enumerate(lines):
    if not any(char == '#' for char in line):
        row_expansion.append(i)


def solve(part_two=False):
    exp_size = 1e6 if part_two else 2
    galaxies = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == '#':
                row_expansion_idx = 0
                while row_expansion[row_expansion_idx] <= i:
                    row_expansion_idx += 1
                    if row_expansion_idx == len(row_expansion):
                        break
                col_expansion_idx = 0
                while col_expansion[col_expansion_idx] <= j:
                    col_expansion_idx += 1
                    if col_expansion_idx == len(col_expansion):
                        break
                galaxies.append((i + (row_expansion_idx * (exp_size - 1)),
                                 j + (col_expansion_idx * (exp_size - 1))))

    total = 0
    for a, b in combinations(galaxies, 2):
        dist = abs(a[0] - b[0]) + abs(a[1] - b[1])
        total += dist
    return total


# Part one
print(solve())
# Part two
print(solve(part_two=True))
