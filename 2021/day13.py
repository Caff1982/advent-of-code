import numpy as np
import matplotlib.pyplot as plt


with open('inputs/input_day13.txt') as f:
    lines = f.read().splitlines()

def fold(points, axis, n):
    new_points = set()
    if axis == 'y':
        for p in points:
            if p[1] > n:
                new_points.add((p[0], abs(p[1]- (2 * n))))
            else:
                new_points.add(p)
    else:
        for p in points:
            if p[0] > n:
                new_points.add((abs(p[0]- (2 * n)), p[1]))
            else:
                new_points.add(p)
    return new_points


points = set()
folds = []
for line in lines:
    if line.startswith('fold'):
        axis, n = line.split('=')
        axis = axis[-1]
        n = int(n)
        folds.append((axis, n))
    elif line:
        row, col = map(int, line.split(','))
        points.add((row, col))


for i, (axis, n) in enumerate(folds):
    points = fold(points, axis, n)
    if i == 0:
        print('Part one: ', len(points))

height = max([i[0] for i in points])+1
width = max([i[1] for i in points])+1
arr = np.zeros((width, height))
for i, j in points:
    arr[j][i] = 1

plt.imshow(arr)
plt.show()