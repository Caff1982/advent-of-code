

with open('input_day1.txt') as f:
    lines = list(map(int, f.read().splitlines()))



# Part one 
print(len([i for i in range(len(lines)-1) if lines[i] < lines[i+1]]))


# Part Two
print(len([i for i in range(len(lines)-3) if lines[i] < lines[i+3]]))
