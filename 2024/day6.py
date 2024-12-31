

with open("inputs/input_day6.txt") as f:
    lines = f.read().splitlines()

directions = [(-1,0),(0,1),(1,0),(0,-1)]


def is_in_bounds(row, col):
    return 0 <= row < len(lines) and 0 <= col < len(lines[0])

def move_and_visit(start_pos, directions, obstructions, lines):
    visited = set()
    row, col = start_pos
    dir_idx = 0

    while is_in_bounds(row, col):
        visited.add((row, col))
        new_row, new_col = row + directions[dir_idx][0], col + directions[dir_idx][1]
        if (new_row, new_col) not in obstructions:
            row, col = new_row, new_col
        else:
            dir_idx = (dir_idx + 1) % 4

    return visited

def part_one(lines):
    obstructions = set()
    start_pos = None
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            if lines[row][col] == "#":
                obstructions.add((row, col))
            elif lines[row][col] == "^":
                start_pos = (row, col)

    visited = move_and_visit(start_pos, directions, obstructions, lines)
    return visited, obstructions, start_pos

def part_two(visited, obstructions, start_pos, lines):
    total_obstructions = 0

    for pos in visited:
        temp_obstructions = obstructions.union({pos})
        row, col = start_pos
        dir_idx = 0
        visited_positions = set()

        while is_in_bounds(row, col):
            delta_row, delta_col = directions[dir_idx]
            new_row, new_col = row + delta_row, col + delta_col
            if (new_row, new_col) in temp_obstructions:
                if (new_row, new_col, delta_row, delta_col) in visited_positions:
                    total_obstructions += 1
                    break

                visited_positions.add((new_row, new_col, delta_row, delta_col))
                dir_idx = (dir_idx + 1) % 4
            else:
                row, col = new_row, new_col

    return total_obstructions


visited, obstructions, start_pos = part_one(lines)
print(len(visited))
total_obstructions = part_two(visited, obstructions, start_pos, lines)
print(total_obstructions)
