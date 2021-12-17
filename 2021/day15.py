import heapq


with open('inputs/input_day15.txt') as f:
    lines = f.read().splitlines()
    grid = [list(map(int, line)) for line in lines]





def solve(grid, visited={}, path={}):
    end = (len(grid)-1, len(grid[0])-1)
    frontier = []
    heapq.heappush(frontier, (0, (0,0)))
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited[(0,0)] = 0
    current = None
    while current != end:
        current = heapq.heappop(frontier)[1]
        for dy, dx in moves:
            y, x = current[0] + dy, current[1] + dx
            if 0 <= y < len(grid) and 0 <= x < len(grid[0]) and (y, x) not in visited:
                move_cost = visited[current] + grid[y][x]
                visited[(y, x)] = move_cost
                heapq.heappush(frontier, (move_cost, (y,x)))
                path[(y, x)] = (current[0] - y, current[1] - x)
    print('solution found!')
    count = 0
    current = end
    while current != (0,0):
        count += grid[current[0]][current[1]]
        parent = path[current]
        current = (current[0]+parent[0], current[1]+parent[1])
    print(count)

# solve(grid)

# Part two

def inc_row(row):
    return [1 if i + 1 > 9 else i+1 for i in row]

temp_rows = grid.copy()
for row in temp_rows:
    iter_row = row.copy()
    for _ in range(4):
        iter_row = inc_row(iter_row)
        row.extend(iter_row)
full_grid = temp_rows.copy()
for i in range(4):
    temp_rows = [inc_row(row) for row in temp_rows]
    full_grid.extend(temp_rows)


solve(full_grid)
