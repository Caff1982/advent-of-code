import numpy as np
import matplotlib.pyplot as plt


with open('inputs/input_day10.txt') as f:
    lines = f.read().splitlines()

operations = []
for line in lines:
    if line == 'noop':
        operations.append(0)
    else:
        operations.append(0)
        operations.append(int(line.split()[1]))

positions = np.cumsum([1] + operations)
print(sum(positions[19::40] * np.arange(20, len(positions), 40)))

# Part two
row_idx = np.arange(len(positions)) % 40
sprites = np.where((row_idx == positions-1) | \
                  (row_idx == positions) | \
                  (row_idx == positions+1))
screen = np.zeros((240))
screen[sprites] = 1
screen = screen.reshape(6, 40)
# Shows "FBURHZCH"
plt.imshow(screen, cmap='binary')
plt.show()