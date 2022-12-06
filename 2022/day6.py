

with open('inputs/input_day6.txt') as f:
    datastream = f.read()


def get_marker(datastream, n):
    for i in range(n, len(datastream)+1):
        if len(set(datastream[i-n:i])) == n:
            return i


print('Part one: ', get_marker(datastream, 4))

print('Part two: ', get_marker(datastream, 14))