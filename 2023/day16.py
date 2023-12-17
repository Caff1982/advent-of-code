from collections import defaultdict
import sys
sys.setrecursionlimit(10000)


with open('inputs/input_day16.txt', 'r') as f:
    grid = f.read().split('\n')


def in_bounds(row, col, grid):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def solve(pos, direction, grid, seen):
    if pos in seen and direction in seen[pos]:
        return seen

    seen[pos].add(direction)

    y, x = pos
    dy, dx = direction
    new_y, new_x = y + dy, x + dx
    if not in_bounds(new_y, new_x, grid):
        return seen

    elif grid[new_y][new_x] == '.':
        return solve((new_y, new_x), direction, grid, seen)
    elif grid[new_y][new_x] == '-':
        if direction in ((-1, 0), (1, 0)):
            return solve((new_y, new_x), (0, 1), grid, seen) | \
                   solve((new_y, new_x), (0, -1), grid, seen)
        else:
            solve((new_y, new_x), direction, grid, seen)
    elif grid[new_y][new_x] == '|':
        if direction in ((0, -1), (0, 1)):
            return solve((new_y, new_x), (1, 0), grid, seen) | \
                   solve((new_y, new_x), (-1, 0), grid, seen)
        else:
            solve((new_y, new_x), direction, grid, seen)
    elif grid[new_y][new_x] == '/':
        if direction == (1, 0):
            return solve((new_y, new_x), (0, -1), grid, seen)
        elif direction == (0, 1):
            return solve((new_y, new_x), (-1, 0), grid, seen)
        elif direction == (-1, 0):
            return solve((new_y, new_x), (0, 1), grid, seen)
        else:
            return solve((new_y, new_x), (1, 0), grid, seen)
    elif grid[new_y][new_x] == '\\':
        if direction == (1, 0):
            return solve((new_y, new_x), (0, 1), grid, seen)
        elif direction == (0, 1):
            return solve((new_y, new_x), (1, 0), grid, seen)
        elif direction == (-1, 0):
            return solve((new_y, new_x), (0, -1), grid, seen)
        else:
            return solve((new_y, new_x), (-1, 0), grid, seen)

    return seen


# TODO: Refactor so that we get direction from first cell
seen = solve((0, 0), (1, 0), grid, defaultdict(set))
print(len(seen))

# Part 2

max_tiles = 0
for row in range(len(grid)):
    pos = (row, 0)
    direction = (0, 1)
    seen = solve(pos, direction, grid, defaultdict(set))
    max_tiles = max(max_tiles, len(seen))

for col in range(len(grid[0])):
    pos = (0, col)
    direction = (1, 0)
    seen = solve(pos, direction, grid, defaultdict(set))
    max_tiles = max(max_tiles, len(seen))

for row in range(len(grid)):
    pos = (row, len(grid[0]) - 1)
    direction = (0, -1)
    seen = solve(pos, direction, grid, defaultdict(set))
    max_tiles = max(max_tiles, len(seen))

for col in range(len(grid[0])):
    pos = (len(grid) - 1, col)
    direction = (-1, 0)
    seen = solve(pos, direction, grid, defaultdict(set))
    max_tiles = max(max_tiles, len(seen))

print(max_tiles)
