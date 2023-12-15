from collections import defaultdict, OrderedDict


def string_to_hash(string):
    hash_sum = 0
    for char in string:
        hash_sum = (hash_sum + ord(char)) * 17 % 256
    return hash_sum


with open('inputs/input_day15.txt', 'r') as f:
    lines = f.read().split(',')

total = sum(string_to_hash(step) for step in lines)
print(total)

# Part 2

results = defaultdict(OrderedDict)
for line in lines:
    if '=' in line:  # Add operation
        label, focal_length = line.split('=')
        box_id = string_to_hash(label)
        focal_length = int(focal_length)
        results[box_id][label] = focal_length
    else:  # Assuming a '-' operator
        label = line[:-1]
        box_id = string_to_hash(label)
        if results.get(box_id) and results[box_id].get(label):
            del results[box_id][label]

total = sum((k + 1) * i * v for k, v_dict in results.items()
            for i, v in enumerate(v_dict.values(), start=1))
print(total)
