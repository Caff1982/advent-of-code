

with open('inputs/input_day4.txt') as f:
    lines = f.read().splitlines()


count = 0
for line in lines:
    area1, area2 = line.split(',')
    start1, end1 = map(int, area1.split('-'))
    start2, end2 = map(int, area2.split('-'))
    if (start1 <= start2 and end1 >= end2) or \
       (start2 <= start1 and end2 >= end1):
       count += 1

print('Part one: ', count)

count = 0
for line in lines:
    area1, area2 = line.split(',')
    start1, end1 = map(int, area1.split('-'))
    start2, end2 = map(int, area2.split('-'))
    if (start1 <= start2 <= end1) or (start2 <= start1 <= end2):
        count += 1

print('Part two: ', count)