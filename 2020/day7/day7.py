
color_dict = {}
with open('day7.txt') as f:
    for line in f.read().splitlines():
        key = line.split(' bags')[0]
        values = [' '.join(i.split()[1:3]) for i in line.split('contain ')[1].split(',')]
        color_dict[key] = values



def can_hold(target_color):
    for color, contents in color_dict.items():
        if any([c == target_color for c in contents]):
            yield color
            yield from can_hold(color)

print(len(set(can_hold('shiny gold'))))


### Part Two ###
color_dict = {}
with open('day7.txt') as f:
    for line in f.read().splitlines():
        key = line.split(' bags')[0]
        values = [i.strip() for i in line.split('contain')[1].split(', ')]
        if values[0] == 'no other bags.':
            color_dict[key] = []
        else:
            color_dict[key] = [{'count': int(i[:1]), 'name': ' '.join(i[2:].split()[:-1])} for i in values]

def get_contents(color):
    return 1 + sum([i['count'] * get_contents(i['name']) for i in color_dict[color]])


print(get_contents('shiny gold') - 1)
