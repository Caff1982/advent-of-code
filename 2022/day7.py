from collections import defaultdict


with open('inputs/input_day7.txt') as f:
    lines = f.read().splitlines()

# Parse file-system structure to dict mapping
# path: dir-size, for all directories
filesystem = defaultdict(int)
idx = 0
path = []
used = 0 # Used memory for part2
while idx < len(lines):
    if lines[idx] == '$ cd ..':
        path.pop()
    elif lines[idx].startswith('$ cd '):
        path.append(lines[idx].split()[2])
    elif lines[idx][0].isnumeric():
        file_size = int(lines[idx].split()[0])
        filesystem[tuple(path)] += file_size
        used += file_size
        if len(path) > 2:
            # Add this file-size to all its parent dirs
            for i in range(2, len(path)):
                filesystem[tuple(path[:i])] += file_size
    idx += 1

# Part one
print(sum([i for i in filesystem.values() if i <= 100000]))

# Part two
free = 70000000 - used
required = 30000000 - free
print(min([i for i in filesystem.values() if i > required]))
