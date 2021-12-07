
with open('input_day7.txt') as f:
    arr = list(map(int, f.read().split(',')))


# Part One
arr.sort()
median = arr[len(arr)//2]
print(sum([abs(median - i) for i in arr]))


# Part Two
mean = (sum(arr) // len(arr))
print(sum([(abs(mean-i)*(abs(mean-i)+1))//2 for i in arr]))

