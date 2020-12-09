import numpy as np


with open('day3.txt') as f:
    arr = f.read().splitlines()


# ### Part One ###
n_trees = 0
for y in range(len(arr)):
    if arr[y][(y*3) % len(arr[0])] == '#':
        n_trees += 1

print(n_trees)


### Part Two ###
def get_num_trees(y_delta, x_delta):
    n_trees = 0
    for y in range(0, len(arr), y_delta):
        if arr[y][((y * x_delta) // y_delta) % len(arr[0])] == '#':
            n_trees += 1
    return n_trees


directions = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
n_trees = []
for y_delta, x_delta in directions:
    n_trees.append(get_num_trees(y_delta, x_delta))

print(np.prod(n_trees))
