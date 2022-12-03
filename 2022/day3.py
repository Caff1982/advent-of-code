import string


with open('inputs/input_day3.py') as f:
    lines = f.read().splitlines()

# ascii_letters used to get item priority
letters = string.ascii_letters
total_priority = 0
for line in lines:
    split_idx = len(line) // 2
    # Split line and convert to sets
    a, b = set(line[:split_idx]), set(line[split_idx:])
    # Intersection used to get find common item
    item = (a & b).pop()
    # Index method used to get item priority
    priority = string.ascii_letters.index(item) + 1
    total_priority += priority

print('Part one: ', total_priority)

total_priority = 0
for i in range(0, len(lines), 3):
    group = [set(line) for line in lines[i:i+3]]
    common = (group[0] & group[1] & group[2]).pop()
    total_priority += letters.index(common) + 1

print('Part two: ', total_priority)
