from collections import defaultdict
import re


"""
TODO: Write a "get_crates" function, call for both
part 1 and part 2. We have correct answers, just 
need to refactor
"""

with open('inputs/input_day5.txt') as f:
    lines = f.read()

stack, instructions = lines.split('\n\n')

def get_crates():
    crates = defaultdict(list)
    for line in reversed(stack.splitlines()[:-1]):
        for i, box in enumerate(line[1::4]):
            if box.isalpha():
                crates[i].append(box)
    return crates

crates = get_crates()
for row in instructions.splitlines():
    n, from_crate, to_crate = map(int, re.findall(r'\d+', row))
    from_crate -= 1
    to_crate -= 1
    crates[to_crate].extend(reversed(crates[from_crate][-n:]))
    crates[from_crate] = crates[from_crate][:-n]

print('Part one: ', ''.join([crates[i][-1] for i in range(len(crates))]))

crates = get_crates()
for row in instructions.splitlines():
    n, from_crate, to_crate = map(int, re.findall(r'\d+', row))
    from_crate -= 1
    to_crate -= 1
    crates[to_crate].extend(crates[from_crate][-n:])
    crates[from_crate] = crates[from_crate][:-n]

print('Part two: ', ''.join([crates[i][-1] for i in range(len(crates))]))