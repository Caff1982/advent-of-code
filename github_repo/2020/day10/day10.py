

with open('day10.txt') as f:
    arr = sorted(list(map(int, f.read().splitlines())))

arr.insert(0, 0)
arr.append(arr[-1] + 3)
ones = 0
threes = 0
for i in range(len(arr)-1):
    if arr[i+1] - arr[i] == 1:
        ones += 1
    else:
        threes += 1

print(ones * threes)


### Part Two ###

def count_ways(arr, idx, cache={}):
    # Base-case, last number has only one solution
    if idx == len(arr) - 1:
        return 1

    if idx in cache:
        return cache[idx]

    ways = 0
    for j in range(idx+1, min(idx+4, len(arr))):
        if arr[j] - arr[idx] <= 3:
            ways += count_ways(arr, j)

    cache[idx] = ways
    return ways

print(count_ways(arr, 0))




