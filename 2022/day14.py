import numpy as np
import matplotlib.pyplot as plt


with open('inputs/input_day14.txt') as f:
    lines = f.read().splitlines()

# lines = """498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9""".splitlines()
# print(lines)


def create_grid(lines, height=250, width=750):
    grid = np.zeros((height, width))
    for line in lines:
        line = line.split(' -> ')
        for i in range(len(line)-1):
            start, end = line[i], line[i+1]
            a_x, a_y = map(int, start.split(','))
            b_x, b_y = map(int, end.split(','))
            if a_x == b_x:
                for dy in range(min(a_y, b_y), max(a_y, b_y)+1):
                    grid[dy][a_x] = 1
            else:
                for dx in range(min(a_x, b_x), max(a_x, b_x)+1):
                    grid[a_y][dx] = 1
    return grid

def solve_p1(grid):
    unit = 0
    while True:
        y, x = -1, 500
        # First veritcal fall
        y = np.argmax(grid[:, x]) - 1
        while True:
            # Try fall diag-left
            if grid[y+1, x-1] == 0:
                y += 1
                x -= 1
                try:
                    while grid[y+1, x] == 0:
                        y += 1
                except IndexError:
                    # End of grid, solution found
                    return unit
            # Try fall diag-right
            elif grid[y+1, x+1] == 0:
                y += 1
                x += 1
                try:
                    while grid[y+1, x] == 0:
                        y += 1
                except IndexError:
                    return unit
            else:
                grid[y, x] = 2
                break

        unit += 1

grid = create_grid(lines)
print('Part one: ', solve_p1(grid))


def solve_p2(grid):
    unit = 0
    while True:
        y, x = -1, 500
        # First fall to obstacle
        y = np.argmax(grid[:, x]) - 1
        if y == -1: # If no move down solution found
            return unit

        while True:
            # Try fall diag-left
            if grid[y+1, x-1] == 0:
                y += 1
                x -= 1
                try:
                    while grid[y+1, x] == 0:
                        y += 1
                except IndexError:
                    pass
            elif grid[y+1, x+1] == 0:
                y += 1
                x += 1
                try:
                    while grid[y+1, x] == 0:
                        y += 1
                except IndexError:
                    pass
            else:
                grid[y, x] = 2
                # plt.imshow(grid[:, 490:510])
                # plt.savefig(f'images/step_{unit}.png')
                break

        unit += 1


grid = create_grid(lines)
# Add floor to grid
max_y = np.where(grid.sum(axis=1) > 0)[0].max()
grid[max_y + 2, :] = 1

print('Part two: ', solve_p2(grid))