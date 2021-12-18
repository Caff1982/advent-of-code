import math
from itertools import permutations


def read_line(line):
    depth = 0
    arr = []
    for char in line:
        if char == '[':
            depth += 1
        elif char == ']':
            depth -= 1
        elif char.isnumeric():
            arr.append([int(char), depth])
    return arr

def reduce_arr(arr):
    # check for explode
    for i, (n, depth) in enumerate(arr):
        if depth >= 5:
            if i > 0:
                arr[i-1][0] += n
            if i < len(arr)-2:
                arr[i+2][0] += arr[i+1][0]
            arr[i:i+2] = [[0, depth-1]]
            return reduce_arr(arr)
    # check for split
    for i, (n, depth) in enumerate(arr):
        if n >= 10:
            x = n / 2
            a, b = math.floor(x), math.ceil(x)
            arr[i] = [b, depth+1]
            arr.insert(i, [a, depth+1])
            return reduce_arr(arr)
    return arr

def add_nums(a, b):
    return[[n, depth+1] for n, depth in a+b]

def get_magnitude(arr):
    while len(arr) > 1:
        for i in range(len(arr)-1):
            if arr[i][1] == arr[i+1][1]:
                arr[i:i+2] = [[3*arr[i][0] + 2*arr[i+1][0], arr[i][1]-1]]
                break
    return arr[0][0]


with open('inputs/input_day18.txt') as f:
    nums = f.read().splitlines()

num = read_line(nums[0])
for line in nums[1:]:
    num = reduce_arr(add_nums(num, read_line(line)))

print(get_magnitude(num))

# Part two
nums = [read_line(line) for line in nums]
max_val = 0
for a, b in permutations(nums, r=2):
    val = get_magnitude(reduce_arr(add_nums(a, b)))
    max_val = max(max_val, val)
print(max_val)