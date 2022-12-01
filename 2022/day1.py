

with open('inputs/input_day1.txt') as f:
    lines = f.read().splitlines()

calorie_arr = []
temp_val = 0
for line in lines:
    if line == '':
        calorie_arr.append(temp_val)
        temp_val = 0
    else:
        temp_val += int(line)

# Part one answer
print(max(calorie_arr))

# Part two answer
print(sum(sorted(calorie_arr)[-3:]))