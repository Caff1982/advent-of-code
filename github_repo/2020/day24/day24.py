from collections import Counter


def get_neighbors(cell):
    dirs = [(2, 0), (1, 1), (-1, 1),
            (-2, 0), (-1, -1), (1, -1)]
    neighbors = []
    for dy, dx in dirs:
        neighbors.append((cell[0] + dy, cell[1] + dx))
    return neighbors


def solve(lines):
    # Idea from https://www.redblobgames.com/grids/hexagons/
    dirs = {'e': (2, 0), 'se': (1, 1), 'sw': (-1, 1),
            'w': (-2, 0), 'nw': (-1, -1), 'ne': (1, -1)}
    visited = []
    for line in lines:
        pos = (0, 0)
        i = 0
        while i < len(line):
            if line[i] in ('s', 'n'):
                dy, dx = dirs[line[i:i+2]]
                pos = (pos[0] + dy, pos[1] + dx)
                i += 2
            else:
                dy, dx = dirs[line[i]]
                pos = (pos[0] + dy, pos[1] + dx)
                i += 1
        visited.append(pos)

    black_squares = [k for k, v in Counter(visited).items() if v % 2]
    print('Part one: ', len(black_squares)) 

    ### Part Two ###
    for _ in range(100):
        all_neighbors = []
        for pos in black_squares:
            all_neighbors.extend(get_neighbors(pos))

        black_squares = [pos for pos, count in Counter(all_neighbors).items() \
                         if (pos in black_squares and count == 1) or count == 2]
       
    print('Part two: ', len(black_squares))


with open('day24.txt') as f:
    lines = f.read().split('\n')

solve(lines)