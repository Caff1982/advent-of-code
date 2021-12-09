

with open('inputs/input_day9.txt') as f:
    grid = [list(map(int, line)) for line in f.read().splitlines()]


# Part One
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
points = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        is_min = True
        for dy,dx in dirs:
            if 0 <= i+dy < len(grid) and 0 <= j+dx < len(grid[0]):
                if grid[i+dy][j+dx] <= grid[i][j]:
                    is_min = False
                    break
        if is_min:
            points.append(grid[i][j]+1)

print(sum(points))


# Part Two
visited = set()

def get_neighbors(row, col):
    neighbs = []
    for dy, dx in dirs:
        new_y, new_x = row+dy, col+dx
        if 0 <= new_y < len(grid) and 0 <= new_x < len(grid[0]):
            neighbs.append((new_y, new_x))
    return neighbs

def get_size(row, col):
    stack = [(row, col)]
    size = 0
    while stack:
        i, j = stack.pop()
        if (i, j) not in visited and grid[i][j] != 9:
            visited.add((i, j))
            size += 1
            stack.extend(get_neighbors(i, j))
    
    return size

sizes = []
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] != 9 and (row, col) not in visited:
            sizes.append(get_size(row, col))

summation = 1
for s in sorted(sizes)[-3:]:
    summation *= s
print(summation)