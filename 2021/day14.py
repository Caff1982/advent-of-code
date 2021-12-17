from collections import Counter


with open('inputs/input_day14.txt') as f:
    lines = f.read().splitlines()

template = lines[0]
pair_dict = {}
for line in lines[2:]:
    a, b = line.split(' -> ')
    pair_dict[a] = b

counter = Counter(a+b for a, b in zip(template, template[1:]))

def step(counter):
    new_counter = Counter()
    for k, v in counter.items():
        new_counter[k[0] + pair_dict[k]] += v
        new_counter[pair_dict[k] + k[1]] += v
    return new_counter

def get_item_diff(counter):
    elem_count = Counter()
    # Add first & last letter from template as these are missing
    elem_count[template[0]] += 1 
    elem_count[template[-1]] += 1
    for k, v in counter.items():
        elem_count[k[0]] += v
        elem_count[k[1]] += v
    return elem_count.most_common()[0][1]//2 - elem_count.most_common()[-1][1]//2

for i in range(40):
    counter = step(counter)
    if i == 9:
        print('Part one: ', get_item_diff(counter))

print('Part two: ', get_item_diff(counter))
