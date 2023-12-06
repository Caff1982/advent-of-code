import math


lines = """Time:      7  15   30
Distance:  9  40  200""".splitlines()

with open('inputs/input_day6.txt', 'r') as f:
    lines = f.read().splitlines()

times = list(map(int, lines[0].split()[1:]))
distances = list(map(int, lines[1].split()[1:]))

total_times = []
for time, dist in zip(times, distances):
    temp_count = 0
    for t in range(time + 1):
        if (time - t) * t > dist:
            temp_count += 1

    total_times.append(temp_count)

print(math.prod(total_times))

# Part 2

time = int(''.join(lines[0].split()[1:]))
distance = int(''.join(lines[1].split()[1:]))

total = 0
for t in range(time + 1):
    if (time - t) * t > distance:
        total += 1

print(total)
