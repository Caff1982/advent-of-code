

def calculate_polygon_area(coordinates, b):
    """
    Calculates the area of a polygon given its coordinates and
    the number of boundary points, 'b'. Uses Pick's theorem.
    """
    # Calculate the number of lattice points inside the polygon
    num_interior_points = 0
    for i in range(len(coordinates)):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[(i + 1) % len(coordinates)]
        num_interior_points += (x2 - x1) * (y2 + y1)

    num_interior_points = abs(num_interior_points) // 2
    # Calculate the area of the polygon using Pick's theorem
    area = num_interior_points - b // 2 + 1 + b
    return area


with open('inputs/input_day18.txt') as f:
    lines = f.read().splitlines()


directions = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
}

pos = (0, 0)
cells = [pos]
b = 0
for line in lines:
    direction, steps, color = line.split()
    pos = (pos[0] + directions[direction][0] * int(steps),
           pos[1] + directions[direction][1] * int(steps))
    cells.append(pos)
    b += int(steps)


print(calculate_polygon_area(cells, b))

# Part 2

directions = {
    '0': (0, 1),
    '2': (0, -1),
    '3': (-1, 0),
    '1': (1, 0)
}

pos = (0, 0)
cells = [pos]
b = 0
for line in lines:
    _, _, color_str = line.split()
    dist = int(color_str[2:-2], 16)
    drows, dcols = directions[color_str[-2:-1]]
    pos = (pos[0] + drows * dist,
           pos[1] + dcols * dist)
    cells.append(pos)
    b += dist

print(calculate_polygon_area(cells, b))
