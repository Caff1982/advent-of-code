
groups = []
temp_str = ''
with open('day6.txt') as f:
    for line in f.read().splitlines():
        if line == '':
            groups.append(len(set(temp_str)))
            temp_str = ''
        else:
            temp_str += line
    groups.append(len(set(temp_str)))

print(sum([group for group in groups]))


### Part Two ### 
group_common = []
temp = []
with open('day6.txt') as f:
    for line in f.read().splitlines():
        if line != '':
            temp.append(set(line))
        else:
            group_common.append(len(set.intersection(*temp)))
            temp = []

    temp.append(set(line))
    group_common.append(len(set.intersection(*temp)))

print(sum(group_common))