

with open('inputs/input_day11.txt') as f:
    lines = f.read().splitlines()
    grid = [list(map(int, line)) for line in lines]


def update_flashes(row, col):
    dirs = [(-1,0), (-1,1), (0,1), (1,1),
            (1,0), (1,-1), (0,-1), (-1,-1)]
    flashed = []
    for dy, dx in dirs:
        y, x = row+dy, col+dx
        if 0 <= y < 10 and 0 <= x < 10:
            grid[y][x] += 1
            if grid[y][x] == 10:
                flashed.append((y, x))
    return flashed


count = 0
iteration = 0
while True:
    flashing = []
    for row in range(10):
        for col in range(10):
            grid[row][col] += 1
            if grid[row][col] == 10:
                flashing.append((row, col))

    for row, col in flashing:
        flashing += update_flashes(row, col)

    count += len(flashing)
    for r, c in flashing:
        grid[r][c] = 0

    if iteration == 99:
        print('Part one: ', count)

    if len(flashing) == 100:
        print('Part two: ', iteration+1)
        break

    iteration += 1