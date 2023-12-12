from functools import cache


with open('inputs/input_day12.txt', 'r') as f:
    lines = f.read().splitlines()


@cache
def solve(springs, clues, size_count=0):
    if len(springs) == 0:
        if (len(clues) == 0 and size_count == 0) or \
           (len(clues) == 1 and size_count == clues[0]):
            return 1
        else:
            return 0

    spring = springs[0]
    springs = springs[1:]
    clue, *new_clues = clues or [0]
    new_clues = tuple(new_clues)

    if spring == '?':
        return solve('#' + springs, clues, size_count) + \
               solve('.' + springs, clues, size_count)
    elif spring == '#':
        return 0 if size_count > clue else solve(springs, clues, size_count + 1)
    elif spring == '.':
        if size_count == 0:
            return solve(springs, clues, 0)
        elif size_count == clue:
            return solve(springs, new_clues, 0)
        else:
            return 0


total = 0
for line in lines:
    springs, clues = line.split()
    clues = tuple(map(int, clues.split(',')))
    count = solve(springs, clues)
    total += count
print(total)

# Part 2

total = 0
for line in lines:
    springs, clues = line.split()
    clues = tuple(map(int, clues.split(',')))
    springs = '?'.join([springs] * 5)
    clues = clues * 5
    count = solve(springs, clues)
    total += count
print(total)