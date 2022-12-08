import numpy as np


with open('inputs/input_day8.txt') as f:
    grid = [list(row) for row in f.read().splitlines()]
    grid = np.array(grid, dtype=np.int)

# Initialize visible_count to contain the edge trees
visible_count = (2 * len(grid)) + (2 * (len(grid) - 2))
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[0]) -1):
        if any((grid[i][j] > max(grid[:i, j]),
               grid[i][j] > max(grid[i+1:, j]),
               grid[i][j] > max(grid[i, :j]),
               grid[i][j] > max(grid[i, j+1:]))):
            visible_count += 1
# Part one
print(visible_count)


max_visibility = 0
deltas = np.array([[-1, 0], [1, 0], [0, -1], [0, 1]])
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[0]) -1):
        visibility = 1
        for dy, dx in deltas:
            temp_vis = 1
            while grid[i, j] > grid[i+(dy*temp_vis), j+(dx*temp_vis)]:
                temp_vis += 1
                if not ((0 <= (i+(dy*temp_vis)) < len(grid)) and \
                       ((0 <= (j+(dx*temp_vis)) < len(grid[0])))):
                    # If next step is edge cell break look
                    temp_vis -= 1
                    break

            visibility *= temp_vis

        max_visibility = max(max_visibility, visibility)
# Part two
print(max_visibility)