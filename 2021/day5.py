from collections import defaultdict


with open('input_day5.txt') as f:
    lines = f.read().splitlines()

points = defaultdict(int)
for line in lines:
    a, b = [tuple(map(int, i.split(','))) for i in line.split(' -> ')]
    if a[0] == b[0]:
        for i in range(min(a[1], b[1]), max(a[1], b[1])+1):
            points[(a[0], i)] += 1
    elif a[1] == b[1]:
        for i in range(min(a[0], b[0]), max(a[0], b[0])+1):
            points[(i, a[1])] += 1

print(len([i for i in points.values() if i > 1]))


# Part Two
points = defaultdict(int)
for line in lines:
    a, b = [tuple(map(int, i.split(','))) for i in line.split(' -> ')]
    if a[0] == b[0]:
        for i in range(min(a[1], b[1]), max(a[1], b[1])+1):
            points[(a[0], i)] += 1
    elif a[1] == b[1]:
        for i in range(min(a[0], b[0]), max(a[0], b[0])+1):
            points[(i, a[1])] += 1
    else:
        if a[0] < b[0]:
            dx = range(a[0], b[0]+1)
        else:
            dx = range(a[0], b[0]-1, -1)
        if a[1] < b[1]:
            dy = range(a[1], b[1]+1)
        else:
            dy = range(a[1], b[1]-1, -1)

        for x, y in zip(dx, dy):
                points[(x, y)] += 1

print(len([i for i in points.values() if i > 1]))
