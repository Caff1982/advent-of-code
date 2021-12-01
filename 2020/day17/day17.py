

def step(grid):
    new_grid = {}
    for x in range(min([i[0] for i in grid.keys()])-1, max([i[0] for i in grid.keys()])+2):
        for y in range(min([i[1] for i in grid.keys()])-1, max([i[1] for i in grid.keys()])+2):
            for z in range(min([i[2] for i in grid.keys()])-1, max([i[2] for i in grid.keys()])+2):
                neighbours = 0
                this_sq = grid.get((x, y, z), False)
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        for dz in (-1, 0, 1):
                            if dx == dy == dz == 0:
                                continue
                            if grid.get((x+dx, y+dy, z+dz), False):
                                neighbours += 1

                if this_sq and neighbours in (2, 3) or not this_sq and neighbours == 3:
                    new_grid[(x, y, z)] = True

    return new_grid


with open('day17.txt') as f:
    arr = f.read().splitlines()
   
grid = {}
for row, line in enumerate(arr):
    for col, char in enumerate(line):
        grid[(row, col, 0)] = char == '#'

for i in range(6):
    grid = step(grid)

print(sum(grid.values()))

### Part Two ###
def step(grid):
    new_grid = {}
    for x in range(min([i[0] for i in grid.keys()])-1, max([i[0] for i in grid.keys()])+2):
        for y in range(min([i[1] for i in grid.keys()])-1, max([i[1] for i in grid.keys()])+2):
            for z in range(min([i[2] for i in grid.keys()])-1, max([i[2] for i in grid.keys()])+2):
                for a in range(min([i[3] for i in grid.keys()])-1, max([i[3] for i in grid.keys()])+2):
                    neighbours = 0
                    this_sq = grid.get((x, y, z, a), False)
                    for dx in (-1, 0, 1):
                        for dy in (-1, 0, 1):
                            for dz in (-1, 0, 1):
                                for da in (-1, 0, 1):
                                    if dx == dy == dz == da == 0:
                                        continue
                                    if grid.get((x+dx, y+dy, z+dz, a+da), False):
                                        neighbours += 1

                    if this_sq and neighbours in (2, 3) or not this_sq and neighbours == 3:
                        new_grid[(x, y, z, a)] = True

    return new_grid

grid = {}
for row, line in enumerate(arr):
    for col, char in enumerate(line):
        grid[(row, col, 0, 0)] = char == '#'

for i in range(6):
    grid = step(grid)

print(sum(grid.values()))