import re
from collections import defaultdict


with open('inputs/input_day2.txt') as f:
    lines = f.read().splitlines()


def parse_colors_and_numbers(text):
    pattern = r'(\d+)\s+(red|green|blue)'
    matches = re.findall(pattern, text)
    return {color: int(number) for number, color in matches}

# Part 1
total = 0
max_values = {'red': 12, 'green': 13, 'blue': 14}
for i, line in enumerate(lines, start=1):
    games = line.split(": ")[1]
    is_valid = True
    for game in games.split("; "):
        game_dict = parse_colors_and_numbers(game)
        for color, max_value in max_values.items():
            if game_dict.get(color, 0) > max_value:
                is_valid = False
                break
        if not is_valid:
            break
    if is_valid:
        total += i

print('Part one: ', total)

# Part 2
total = 0
colors = ('red', 'green', 'blue')
for line in lines:
    temp_dict = defaultdict(int)
    games = line.split(": ")[1]
    for game in games.split("; "):
        game_dict = parse_colors_and_numbers(game)
        for color in colors:
            temp_dict[color] = max(temp_dict[color], game_dict.get(color, 0))

    power = temp_dict['red'] * temp_dict['green'] * temp_dict['blue']
    total += power

print('Part two: ', total)
