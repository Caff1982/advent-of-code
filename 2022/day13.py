from functools import cmp_to_key


with open('inputs/input_day13.txt') as f:
    lines = [eval(line) for line in f.read().splitlines() if line.strip()]


def check_order(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1 # Correct
        elif right < left:
            return 1 # Wrong
        else:
            return 0

    elif isinstance(left, list) and isinstance(right, list):
        for a, b in zip(left, right):
            ret = check_order(a, b)
            if ret != 0:
                return ret
        return check_order(len(left), len(right))

    elif isinstance(left, list) and isinstance(right, int):
        return check_order(left, [right])

    elif isinstance(left, int) and isinstance(right, list):
        return check_order([left], right)


count = 0
idx = 1
for i in range(0, len(lines), 2):
    if check_order(lines[i], lines[i+1]) <= 0:
        count += idx
    idx +=1

print('Part one: ', count)


lines.extend([[[2]], [[6]]])
sorted_lines = sorted(lines, key=cmp_to_key(check_order))
a = sorted_lines.index([[2]]) + 1
b = sorted_lines.index([[6]]) + 1
print('Part two: ', a * b)