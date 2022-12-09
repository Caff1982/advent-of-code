

with open('inputs/input_day9.txt') as f:
    lines = f.read().splitlines()


def solve(lines, n):
    move_dict = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }
    knots = [[0, 0] for _ in range(n)]
    visited = []
    for line in lines:
        move, n_moves = line.split()
        for _ in range(int(n_moves)):
            knots[0][0] += move_dict[move][0]
            knots[0][1] += move_dict[move][1]
            for i in range(1, len(knots)):
                dy = knots[i-1][0] - knots[i][0]
                dx = knots[i-1][1] - knots[i][1]
                if abs(dy) > 1 or abs(dx) > 1:
                    dy = dy // abs(dy) if dy else 0
                    dx = dx // abs(dx) if dx else 0
                    knots[i][0] += dy
                    knots[i][1] += dx

            visited.append(tuple(knots[-1]))

    print(len(set(visited)))

# Part one
solve(lines, 2)
# Part two
solve(lines, 10)