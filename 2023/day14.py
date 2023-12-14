

def load_grid():
    with open('inputs/input_day14.txt', 'r') as f:
        grid = f.read().splitlines()
        grid = [list(line) for line in grid]
    return grid

def tilt(grid):
    top_cols = [0] * len(grid[0])
    for col in range(len(grid[0])):
        for row in range(len(grid)):
            if grid[row][col] == '#':
                top_cols[col] = row + 1
            elif grid[row][col] == 'O':
                top_cols[col] += 1
                grid[row][col] = '.'
                grid[top_cols[col] - 1][col] = 'O'
    return grid

def calculate_weight(grid):
    total = 0
    n_rows = len(grid)
    for i, row in enumerate(grid):
        weight = n_rows - i
        total += weight * row.count('O')
    return total

def rotate_grid(grid):
    # Rotate 90 degrees clockwise
    return [list(reversed(col)) for col in zip(*grid)]

def perform_one_cycle(grid):
    grid = tilt(grid)
    grid = rotate_grid(grid)
    grid = tilt(grid)
    grid = rotate_grid(grid)
    grid = tilt(grid)
    grid = rotate_grid(grid)
    grid = tilt(grid)
    grid = rotate_grid(grid)
    return grid


grid = load_grid()
grid = tilt(grid)
print(calculate_weight(grid))

# Part 2

grid = load_grid()
results_dict = {}
i = 0
n_cycles = 1000000000
while i < n_cycles:
    grid = perform_one_cycle(grid)
    grid_key = tuple(tuple(row) for row in grid)
    if grid_key in results_dict:
        cycle = i - results_dict[grid_key]
        i += cycle * ((n_cycles - i) // cycle)
    else:
        results_dict[grid_key] = i

    i += 1

print(calculate_weight(grid))
