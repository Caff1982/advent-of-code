

with open('input_day6.txt') as f:
    lines = f.read()

# Part One
arr = map(int, lines.split(','))
for day in range(80):
    new_arr = []
    for i in arr:
        if i == 0:
            new_arr.extend([6, 8])
        else:
            new_arr.append(i-1)
    arr = new_arr

print(len(arr))


# Part Two
arr = map(int, lines.split(','))
age_arr = [0] * 9
for i in arr:
    age_arr[i] += 1

for day in range(256):
    age_arr[(day+7)%9] += age_arr[day%9]

print(sum(age_arr))

