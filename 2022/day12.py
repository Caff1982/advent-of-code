from collections import deque


with open('inputs/input_day12.txt') as f:
    lines = f.read().splitlines()


def get_neighbors(grid, node):
    neighbors = []
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        y, x = node[0] + dy, node[1] + dx
        if (0 <= y < len(grid)) and (0 <= x < len(grid[0])):
            neighbors.append((y, x))
    return neighbors
    
def solve_p1(grid, start, end):
    frontier = deque([(start, 0)])
    visited = {}
    visited[start] = None
    while True:
        current, dist = frontier.popleft()
        if current == end:
            # Solution found
            break
        for n in get_neighbors(grid, current):
            # Check move is valid
            if grid[n[0]][n[1]] - grid[current[0]][current[1]] <= 1 \
               and n not in visited:
                frontier.append((n, dist + 1))
                visited[n] = (current[0] - n[0], current[1] - n[1])
    path = [] 
    while current != start:
        path.append(current)
        parent = visited[current]
        current = (current[0] + parent[0], current[1] + parent[1])
    return len(path)

grid = []
for i in range(len(lines)):
    row = []
    for j in range(len(lines[0])):
        if lines[i][j] == 'S':
            start = (i, j)
            row.append(0)
        elif lines[i][j] == 'E':
            end = (i, j)
            row.append(25)
        else:
            row.append(ord(lines[i][j]) - 97)
    grid.append(row)

print('Part one: ', solve_p1(grid, start, end))


def solve_p2(grid, start):
    frontier = deque([(start, 0)])
    visited = {}
    visited[start] = None
    while True:
        current, dist = frontier.popleft()
        if grid[current[0]][current[1]] == 0:
            # Solution found
            break
        for n in get_neighbors(grid, current):
            # Check move is valid
            if grid[current[0]][current[1]] - grid[n[0]][n[1]] <= 1 \
               and n not in visited:
                frontier.append((n, dist + 1))
                visited[n] = (current[0] - n[0], current[1] - n[1])
    path = [] 
    while current != start:
        path.append(current)
        parent = visited[current]
        current = (current[0] + parent[0], current[1] + parent[1])
    return len(path)

print('Part two: ', solve_p2(grid, end))