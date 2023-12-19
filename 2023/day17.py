import heapq


with open('inputs/input_day17.txt') as f:
    grid = f.read().splitlines()

grid = [list(map(int, row)) for row in grid]

visited = set()
# Priority queue: cost, row, col, drow, dcol, distance
queue = [(0, 0, 0, 0, 0, 0)]
target = (len(grid) - 1, len(grid[0]) - 1)
while queue:
    cost, row, col, drow, dcol, dist = heapq.heappop(queue)
    if (row, col) == target:
        print(cost)
        break
    if (row, col, drow, dcol, dist) in visited:
        continue
    visited.add((row, col, drow, dcol, dist))

    if dist < 3 and (row, col) != (0, 0):  # Can continue in same direction
        nrow, ncol = row + drow, col + dcol
        if 0 <= nrow < len(grid) and 0 <= ncol < len(grid[0]):
            heapq.heappush(queue, (cost + grid[nrow][ncol], nrow, ncol, drow, dcol, dist + 1))

    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)): 
        if (dy, dx) != (-drow, -dcol) and 0 <= row + dy < len(grid) and 0 <= col + dx < len(grid[0]) and (dy, dx) != (drow, dcol):
            heapq.heappush(queue, (cost + grid[row + dy][col + dx], row + dy, col + dx, dy, dx, 1))


# Part 2

visited = set()
queue = [(0, 0, 0, 0, 0, 0)]
target = (len(grid) - 1, len(grid[0]) - 1)
while queue:
    cost, row, col, drow, dcol, dist = heapq.heappop(queue)
    if (row, col) == target and dist >= 4:
        print(cost)
        break
    if (row, col, drow, dcol, dist) in visited:
        continue
    visited.add((row, col, drow, dcol, dist))

    if dist < 10 and (row, col) != (0, 0):
        nrow, ncol = row + drow, col + dcol
        if 0 <= nrow < len(grid) and 0 <= ncol < len(grid[0]):
            heapq.heappush(queue, (cost + grid[nrow][ncol], nrow, ncol, drow, dcol, dist + 1))

    if dist >= 4 or (row, col) == (0, 0):
        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if (dy, dx) != (-drow, -dcol) and (dy, dx) != (drow, dcol) and 0 <= row + dy < len(grid) and 0 <= col + dx < len(grid[0]):
                heapq.heappush(queue, (cost + grid[row + dy][col + dx], row + dy, col + dx, dy, dx, 1))
