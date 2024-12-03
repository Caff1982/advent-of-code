import re


def solve(data):
    pattern = r"mul\((\d+),\s*(\d+)\)"
    matches = re.findall(pattern, data)
    return sum(int(x) * int(y) for x, y in matches)


with open('inputs/input_day3.txt', 'r') as f:
    data = f.read()

print(solve(data))


new_data = []
i = 0
ignore = False
while i < len(data):
    if data[i:i+7] == "don't()":
        ignore = True
        i += 7
    elif data[i:i+4] == "do()":
        ignore = False
        i += 4
    else:
        if not ignore:
            new_data.append(data[i])
        i += 1

print(solve(''.join(new_data)))
