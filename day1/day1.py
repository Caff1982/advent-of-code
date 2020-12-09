from itertools import combinations
import numpy as np

with open('day1.txt', 'r') as f:
    arr_str = f.read().splitlines()

arr = list(map(int, arr_str))
for i in arr:
    target = 2020 - i
    if target in arr:
        print(i * target)
        break


### Part Two ###
arr = list(map(int, arr_str))
combs = list(combinations(arr, r=3))
for comb in combs:
    if sum(comb) == 2020:
        print(np.prod(comb))
        break
