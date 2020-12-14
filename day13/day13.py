import numpy as np


with open('day13.txt') as f:
    arr = f.read().splitlines()

target = int(arr[0])
buses = [int(i) for i in arr[1].split(',') if i != 'x']
delays = [b - (target % b) for b in buses]

min_val = min(delays)
idx = delays.index(min_val)
print(min_val * buses[idx])


### Part Two ###

buses = arr[1].split(',')
# pairs is an array of (divisor, remainder)
pairs = [(int(buses[i]), (int(buses[i]) - i) % int(buses[i])) for i in range(len(buses)) if buses[i] != 'x']

answer = 0
increment = 1
for n, r in pairs:
    while answer % n != r:
        answer += increment
    increment *= n

print(answer)
