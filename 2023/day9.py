

with open('inputs/input_day9.txt', 'r') as f:
    lines = f.readlines()


def get_next_value(line, count=0):
    if all(i == 0 for i in line):
        return count
    else:
        count += line[-1]
        line = [line[i + 1] - line[i] for i in range(len(line) - 1)]
        return get_next_value(line, count)


total = 0
for line in lines:
    line = [int(i) for i in line.split()]
    ans = get_next_value(line)
    total += ans
print(total)

# Part 2

total = 0
for line in lines:
    line = [int(i) for i in line.split()[::-1]]
    ans = get_next_value(line)
    total += ans
print(total)