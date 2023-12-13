import numpy as np

lines = open('inputs/input_day13.txt').read().splitlines()


def get_reflections(grid):
    grid = np.array(grid)
    # Check for symmetry along the x axis
    for x in range(1, len(grid[0])):
        flipped = np.flip(grid[:, :x], axis=1)
        flipped = flipped[:, :min(x, len(grid[0]) - x)]
        if np.array_equal(grid[:, x:min(x + x, len(grid[0]))], flipped):
            return x
    # Check for symmetry along the y axis
    for y in range(1, len(grid)):
        flipped = np.flip(grid[:y, :], axis=0)
        flipped = flipped[:min(y, len(grid) - y), :]
        if np.array_equal(grid[y:min(y + y, len(grid)), :], flipped):
            return y * 100


def get_reflections_part2(grid):
    grid = np.array(grid)
    for x in range(1, len(grid[0])):
        flipped = np.flip(grid[:, :x], axis=1)
        flipped = flipped[:, :min(x, len(grid[0]) - x)]
        if (grid[:, x:min(x + x, len(grid[0]))] != flipped).sum() == 1:
            return x
    for y in range(1, len(grid)):
        flipped = np.flip(grid[:y, :], axis=0)
        flipped = flipped[:min(y, len(grid) - y), :]
        if (grid[y:min(y + y, len(grid)), :] != flipped).sum() == 1:
            return y * 100


grid = []
total_p1 = 0
total_p2 = 0
for line in lines:
    if len(line) > 1:
        grid.append([1 if c == '#' else 0 for c in line])
    else:
        total_p1 += get_reflections(grid)
        total_p2 += get_reflections_part2(grid)
        grid = []

if len(grid) > 0:
    total_p1 += get_reflections(grid)
    total_p2 += get_reflections_part2(grid)
print(total_p1)
print(total_p2)
