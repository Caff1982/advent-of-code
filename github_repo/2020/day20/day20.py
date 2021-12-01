import numpy as np
from collections import defaultdict


class Tile:
    def __init__(self, tile_id, tile):
        self.id = tile_id
        self.tile = tile
        # Borders stored as top, right, bottom, left
        self.edges = [self.tile[0], ''.join(row[-1] for row in self.tile),
                        self.tile[-1][::-1], ''.join(row[0] for row in self.tile)[::-1]]
        self.flipped_edges = [edge[::-1] for edge in self.edges]

    def __repr__(self):
        return '\n'.join(self.tile)


tiles = []
with open('day20.txt') as f:
    for tile in f.read().split('\n\n'):
         tile_id = int(tile[5:9])
         lines = tile.splitlines()[1:]
         tiles.append(Tile(tile_id, lines))

corners = []
for i, tile in enumerate(tiles):
    edges = set(tile.edges)
    for j, other in enumerate(tiles):
        if i == j:
            continue
        for edge in tuple(edges):
            all_edges = set()
            if edge in set(other.edges + other.flipped_edges):
                edges.discard(edge)
    if len(edges) == 2:
        corners.append(tile.id)

print(np.prod(corners))


### Part Two ###
class Tile:
    """
    Edges are stored as Top, Right, Bottom, Left
    """
    def __init__(self, tile_id, tile):
        self.id = tile_id
        self.tile = tile

    def __repr__(self):
        return '\n'.join(self.tile)

    def edges(self):
        return [self.tile[0], ''.join(row[-1] for row in self.tile),
                self.tile[-1], ''.join(row[0] for row in self.tile)]

    def image(self):
        image = []
        for row in range(1, len(self.tile)-1):
            image.append(self.tile[row][1:-1])
        return image

    def rotate(self):
        """
        Rotates tile 90 degress clockwise
        """
        rotated = []
        for i in range(len(self.tile)):
            rotated.append(''.join(row[i] for row in self.tile)[::-1])
        self.tile = rotated
    
    def flip(self):
        """
        Flips tile horizontally 
        """
        self.tile = [row[::-1] for row in self.tile]


    def fits_left(self, edge):
        """
        Checks if border fits the left border of this tile
        """
        for _ in range(4):
            if edge == self.edges()[-1]:
                return True
            self.rotate()
        self.flip()
        for _ in range(4):
            if edge == self.edges()[-1]:
                return True
            self.rotate()
        return False

    def fits_above(self, edge):
        for _ in range(4):
            if edge == self.edges()[0]:
                return True
            self.rotate()
        self.flip()
        for _ in range(4):
            if edge == self.edges()[0]:
                return True
            self.rotate()
        return False

    def fits_left_and_above(self, edge_left, edge_top):
        for _ in range(4):
            if edge_left == self.edges()[-1] and \
               edge_top == self.edges()[0]:
                return True
            self.rotate()
        self.flip()
        for _ in range(4):
            if edge_left == self.edges()[-1] and \
               edge_top == self.edges()[0]:
                return True
            self.rotate()
        return False


def solve(tiles, solution, used, size):
    if len(solution) == len(tiles):
        return solution

    if len(solution) < size: # Check Left
        last_tile = solution[-1]
        last_edge = last_tile.edges()[1]
        for tile_id, tile in tiles.items():
            if tile_id not in used:
                if tile.fits_left(last_edge):
                    solution.append(tile)
                    used.append(tile_id)
                    sol = solve(tiles, solution, used, size)
                    if sol:
                        return sol

    elif len(solution) % size == 0: # New row, check Up
        last_tile = solution[-size]
        last_edge = last_tile.edges()[2]
        for tile_id, tile in tiles.items():
            if tile_id not in used:
                if tile.fits_above(last_edge):
                    solution.append(tile)
                    used.append(tile_id)
                    sol = solve(tiles, solution, used, size)
                    if sol:
                        return sol
    else: # Check left and Up
        top_edge = solution[-size].edges()[2]
        left_edge = solution[-1].edges()[1]
        for tile_id, tile in tiles.items():
            if tile_id not in used:
                if tile.fits_left_and_above(left_edge, top_edge):
                    solution.append(tile)
                    used.append(tile_id)
                    sol = solve(tiles, solution, used, size)
                    if sol:
                        return sol


def count_cells(image, coords):
    monster_cells = set()
    for row in range(len(image)-2):
        for col in range(len(image[0])-19):
            is_monster = True
            for y, x in coords:
                if image[row+y][col+x] != '#':
                    is_monster = False
                    break
            if is_monster:
                for y, x in coords:
                    monster_cells.add((row+y, col+x))
    if len(monster_cells) > 1:
        total_cells = 0
        for row in image:
            total_cells += row.count('#')
        return total_cells - len(monster_cells)

def rotate_image(full_image, monster_coords):
    # Rotates & Flips image to find sea monsters
    for _ in range(4):
        rotated = []
        for i in range(len(full_image)):
            rotated.append(''.join(row[i] for row in full_image)[::-1])
        full_image = rotated
        ret = count_cells(full_image, monster_coords)
        if ret:
            return ret
    # Flip image
    full_image = full_image[::-1]
    for _ in range(4):
        rotated = []
        for i in range(len(full_image)):
            rotated.append(''.join(row[i] for row in full_image)[::-1])
        full_image = rotated
        ret = count_cells(full_image, monster_coords)
        if ret:
            return ret


tiles = {}
with open('day20.txt') as f:
    for tile in f.read().split('\n\n'):
         tile_id = int(tile[5:9])
         lines = tile.splitlines()[1:]
         tiles[tile_id] = Tile(tile_id, lines)

size = int(np.sqrt(len(tiles)))

# Solve puzzle
for tile_id in corners:
    solution = [tiles[tile_id]]
    used = [tile_id]
    solution = solve(tiles, solution, used, size)
    if solution:
        break

# Putting puzzle pieces together
arr = []
for row in range(size):
    arr.append([tile.image() for tile in solution[row*size:row*size+size]])
full_image = []
for row in range(size):
    for i in range(len(arr[0][0])):
        full_image.append(''.join(tile[i] for tile in arr[row]))


# Sea monster dims are 3 x 20
sea_monster = [
    '..................#.',
    '#....##....##....###',
    '.#..#..#..#..#..#...',
]

# Monster coords stores the Y-delta and X-delta for each monster cell
monster_coords = [(i, j) for i in range(len(sea_monster)) for j in range(len(sea_monster[0])) if sea_monster[i][j] == '#']

ans = rotate_image(full_image, monster_coords)
print(ans)