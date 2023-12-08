import math


with open('inputs/input_day8.txt', 'r') as f:
    lines = f.read().splitlines()


map_dict = {}
for line in lines[2:]:
    node, children = line.split(' = ')
    left, right = children[1:-1].split(', ')
    map_dict[node] = (left, right)


instructions = lines[0]
pos = 'AAA'
idx = 0
count = 0
while pos != 'ZZZ':
    left, right = map_dict[pos]
    if instructions[idx] == 'R':
        pos = right
    else:
        pos = left

    idx = (idx + 1) % len(instructions)
    count += 1

print(count)

# Part 2

start_positions = [k for k in map_dict if k.endswith('A')]
distances = []
for pos in start_positions:
    idx = 0
    count = 0
    while pos[-1] != 'Z':
        left, right = map_dict[pos]
        if instructions[idx] == 'R':
            pos = right
        else:
            pos = left

        idx = (idx + 1) % len(instructions)
        count += 1
    distances.append(count)

print(math.lcm(*distances))
