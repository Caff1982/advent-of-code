import re
from collections import defaultdict


with open('day14.txt') as f:
    arr = f.read().splitlines()


def apply_bitmask(mask, arg):
    """
    Use OR to apply 1 from bitmask and
    use AND to apply 0.
    """
    arg = int(arg)
    ones = int(mask.replace('X', '0'), 2)
    arg |= ones
    zeros = int(mask.replace('X', '1'), 2)
    arg &= zeros
    return arg

mem_dict = defaultdict(int)
mask = ''
for line in arr:
    op, arg = line.split(' = ')
    if op == 'mask':
        mask = arg
    else:
        key = int(re.findall(r"\[([\w]+?)\]", op)[0])
        new_value = apply_bitmask(mask, arg)
        mem_dict[key] = new_value

print(sum(mem_dict.values()))


### Part Two ###

def get_all_addresses(location):
    if not 'X' in location:
        yield location
    else:
        yield from get_all_addresses(location.replace('X', '1', 1))
        yield from get_all_addresses(location.replace('X', '0', 1))

mem_dict = defaultdict(int)
mask = ''
for line in arr:
    op, arg = line.split(' = ')
    if op == 'mask':
        mask = arg
    else:
        location = int(re.findall(r"\[([\w]+?)\]", op)[0])
        location_str = format(location, '#038b')[2:]
        masked_loc = ''
        for i in range(len(location_str)):
            if mask[i] == 'X':
                masked_loc += 'X'
            elif mask[i] == '1':
                masked_loc += '1'
            else:
                masked_loc += location_str[i]

        for addr in get_all_addresses(masked_loc):
            mem_dict[int(addr, 2)] = int(arg)


print(sum(mem_dict.values()))