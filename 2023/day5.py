from collections import defaultdict


with open('inputs/input_day5.txt', 'r') as f:
    lines = f.read().splitlines()


seeds = list(map(int, lines[0].split()[1:]))
maps = defaultdict(list)
for line in lines[2:]:
    if line == '':
        continue
    elif line[0].isalpha():
        key = line.split(' map:')[0]
    elif line[0].isdigit():
        maps[key].append(list(map(int, line.split())))


def get_location(seed, maps):
    for k, ranges in maps.items():
        for dest, src, n in ranges:
            if src <= seed < src + n:
                seed = seed + dest - src
                break
    return seed


min_seed = float("inf")
for seed in seeds:
    min_seed = min(min_seed, get_location(seed, maps))
print(min_seed)

# Part 2

min_seed = float("inf")
seen = set()
for i in range(0, len(seeds), 2):
    for seed in range(seeds[i], seeds[i] + seeds[i + 1]):
        if seed in seen:
            continue
        min_seed = min(min_seed, get_location(seed, maps))
        seen.add(seed)
print(min_seed)
