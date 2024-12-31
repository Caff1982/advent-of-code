
with open("inputs/input_day10.txt") as f:
    lines = f.read().splitlines()

grid = [list(map(int, line)) for line in lines]

def find_paths(row, col, visited):
    if grid[row][col] == 9:
        return [visited]
    else:
        all_paths = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) \
               and grid[new_row][new_col] -1 == grid[row][col]:
                all_paths += find_paths(new_row, new_col, visited + [(new_row, new_col)])
        return all_paths

total_p1 = 0
total_p2 = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == 0:
            all_paths = find_paths(row, col, [(row, col)])
            valid_paths = set([t[-1] for t in all_paths])
            total_p1 += len(valid_paths)
            total_p2 += len(all_paths)

print(total_p1)
print(total_p2)
