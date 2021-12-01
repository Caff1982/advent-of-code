import numpy as np

with open('day12.txt') as f:
    arr = f.read().splitlines()

def update_pos(key, value, pos):
    if key == 'N':
        pos[1] += value
    elif key == 'S':
        pos[1] -= value
    elif key == 'E':
        pos[0] += value
    elif key == 'W':
        pos[0] -= value
    return pos

directions = ['E', 'S', 'W', 'N']
pos = [0, 0] # Represents East/West and North/South
current_dir = 0 # Current direction
for row in arr:
    key, value = row[0], int(row[1:])
    if key in directions:
        pos = update_pos(key, value, pos)

    elif key == 'F':
        pos = update_pos(directions[current_dir], value, pos)

    elif key == 'R':
        current_dir = (current_dir + value // 90) % 4
    elif key == 'L':
        current_dir = (current_dir - value // 90) % 4

print(np.sum(np.abs(pos)))


### Part Two ###

directions = ['E', 'S', 'W', 'N']
pos = np.array([0, 0]) # Represents East/West and North/South
waypoint = np.array([10, 1])
for row in arr:
    key, value = row[0], int(row[1:])
    if key in directions:
        waypoint = update_pos(key, value, waypoint)

    elif key == 'F':
        pos += value * waypoint

    elif key == 'R':
        d = value // 90
        if d == 1:
            waypoint = np.array([waypoint[1], -waypoint[0]])
        elif d == 2:
            waypoint *= -1
        elif d == 3:
            waypoint = np.array([-waypoint[1], waypoint[0]])
        else:
            print('Direction: ', d)

    elif key == 'L':
        d = value // 90
        if d == 1:
            waypoint = np.array([-waypoint[1], waypoint[0]])
        elif d == 2:
            waypoint *= -1
        elif d == 3:
            waypoint = np.array([waypoint[1], -waypoint[0]])
        else:
            print('Direction: ', d)

print(np.sum(np.abs(pos)))