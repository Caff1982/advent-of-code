

with open('inputs/input_day2.txt') as f:
    lines = f.read().splitlines()
    

def is_safe(row):
    diffs = set([row[i + 1] - row[i] for i in range(len(row) - 1)])
    if diffs.issubset({1, 2, 3}) or diffs.issubset({-1, -2, -3}):
        return True
    return False


lines = [[int(i) for i in row.split(' ')] for row in lines]
print(sum([is_safe(row) for row in lines]))

total = 0
for row in lines:
    if any([is_safe(row[:i] + row[i + 1:]) for i in range(len(row))]):
        total += 1
print(total)
