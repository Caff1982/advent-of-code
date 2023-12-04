

SYMBOLS = "+$&/%=#*-@"

def is_symbol(cell):
    return cell in SYMBOLS

def is_valid_part(start, end, lines):
    # Check top row
    if start[0] > 0 and any(is_symbol(c) for c in lines[start[0]-1][max(0, start[1]-1):min(end[1]+2, len(lines[0]))]):
        return True
    # Check bottom row
    if start[0] != len(lines)-1 and any(is_symbol(c) for c in lines[start[0]+1][max(0, start[1]-1):min(end[1]+2, len(lines[0]))]):
        return True
    # Check left cell
    if start[1] > 0 and is_symbol(lines[start[0]][start[1]-1]):
        return True
    # Check right cell
    if end[1] != len(lines[0])-1 and is_symbol(lines[start[0]][end[1]+1]):
        return True

    return False


with open('inputs/input_day3.txt') as f:
    lines = f.read().splitlines()

total = 0
for i in range(len(lines)):
    start_index = None
    end_index = None
    for j in range(len(lines[0])):
        if lines[i][j].isdigit() and start_index is None:
            start_index = (i, j)
        elif not lines[i][j].isdigit() and start_index is not None:
            if is_valid_part(start_index, (i, j-1), lines):
                part_num = int(lines[i][start_index[1]:j])
                total += part_num
            start_index = None
    if start_index is not None:
        if is_valid_part(start_index, (i, j), lines):
            part_num = int(lines[i][start_index[1]:j+1])
            total += part_num
        start_index = None
print(total)


# Part 2

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0),
              (1, 1), (1, -1), (-1, 1), (-1, -1)]
GEAR_SYMBOL = '*'


def add_digit(char, current_number_str, adjacent_cells, i, j):
    if char.isdigit():
        current_number_str += char
        for dx, dy in DIRECTIONS:
            adjacent_cells.add((i+dx, j+dy))
    return current_number_str, adjacent_cells


gears = set()
current_number_str = ''
adjacent_cells = set()
numbers = []
total = 0
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        current_number_str, adjacent_cells = add_digit(char, current_number_str, adjacent_cells, i, j)
        if not char.isdigit() and current_number_str:
            numbers.append((int(current_number_str), adjacent_cells))
            current_number_str = ''
            adjacent_cells = set()
        if char == GEAR_SYMBOL:
            gears.add((i, j))
for gear in gears:
    adjacent_numbers = [number for number, cells in numbers if gear in cells]
    if len(adjacent_numbers) == 2:
        total += adjacent_numbers[0] * adjacent_numbers[1]
print(total)
