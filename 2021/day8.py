

with open('inputs/input_day8.txt') as f:
    lines = f.read().splitlines()


# Part One
count = 0
for l in lines:
    values = l.split(' | ')[1]
    count += sum([True if len(i) in (2, 4, 3, 7) else False for i in values.split()])

print(count)


# Part Two
count = 0
for line in lines:
    signal, connections = line.split(' | ')

    digit_dict = {}
    for i in signal.split():
        if len(i) == 2:
            digit_dict[1] = set(i)
        elif len(i) == 3:
            digit_dict[7] = set(i)
        elif len(i) == 4:
            digit_dict[4] = set(i)
        elif len(i) == 7:
            digit_dict[8] = set(i)

    for s in signal.split():
        if len(s) == 5:
            if len(digit_dict[1].difference(set(s))) == 0:
                digit_dict[3] = set(s)
            elif len(digit_dict[4].difference(set(s))) == 1:
                digit_dict[5] = set(s)
            else:
                digit_dict[2] = set(s)
        elif len(s) == 6:
            if len(digit_dict[4].difference(set(s))) == 0:
                digit_dict[9] = set(s)
            elif len(digit_dict[7].difference(set(s))) == 0:
                digit_dict[0] = set(s)
            else:
                digit_dict[6] = set(s)

    set2num_dict = {str(sorted(v)):str(k) for k, v in digit_dict.items()}
    num = int(''.join([set2num_dict[str(sorted(set(i)))] for i in connections.split()]))
    count += num

print(count)