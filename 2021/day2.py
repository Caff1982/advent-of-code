

with open('input_day2.txt') as f:
    lines = f.read().splitlines()

# Part one
h_pos, v_pos = 0, 0
for l in lines:
    comand, val = l.split()
    if comand == 'forward':
        h_pos += int(val)
    elif comand == 'back':
        h_pos -= int(val)
    elif comand == 'up':
        v_pos -= int(val)
    else:
        v_pos += int(val)

print(h_pos * v_pos)

# Part two
aim, h_pos, v_pos = 0, 0, 0
for l in lines:
    comand, val = l.split()
    if comand == 'forward':
        h_pos += int(val)
        v_pos += int(val) * aim
    elif comand == 'back':
        h_pos -= int(val)
    elif comand == 'up':
        aim -= int(val)
    else:
        aim += int(val)

print(h_pos * v_pos)