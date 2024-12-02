
with open('inputs/input_day1.txt') as f:
    lines = f.read().splitlines()


arr1, arr2 = zip(*(map(int, line.split()) for line in lines))

arr1 = sorted(arr1)
arr2 = sorted(arr2)

total = sum(abs(i - j) for i, j in zip(arr1, arr2))
print(total)

# Part two
from collections import Counter

counts = Counter(arr2)
print(sum(counts[i] * i for i in arr1))
