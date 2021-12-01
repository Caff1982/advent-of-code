import re
from collections import defaultdict
    

rule_dict = {}

with open('day16.txt') as f:
    rules, your_ticket, tickets = f.read().split('\n\n')


rules = rules.split('\n')
total_max = 0
total_min = float('inf')
for rule in rules:
    field, limits = rule.split(': ')
    limits = [int(i) for i in re.findall(f'\d+', limits)]
    rule_dict[field] = limits
    if limits[0] < total_min:
        total_min = limits[0]
    elif limits[-1] > total_max:
        total_max = limits[-1]


tickets = tickets.split('\n')[1:]
ans = 0
valid_tix = []
for line in tickets:
    fail = False
    values = list(map(int, line.split(',')))
    for v in values:
        if v < total_min or v > total_max:
            ans += v
            fail = True
            break

    if not fail:
        valid_tix.append(values)

print('Part one answer: ', ans)


### Part Two ###
your_ticket = list(map(int, your_ticket.split('\n')[1].split(',')))

valid_fields= {i: set(rule_dict.keys()) for i in range(len(valid_tix[0]))}
for ticket in valid_tix:
    for i, value in enumerate(ticket):
        for field in rule_dict:
            if not(rule_dict[field][0] <= value <= rule_dict[field][1]) \
            and not(rule_dict[field][2] <= value <= rule_dict[field][3]):
                valid_fields[i].discard(field)

for i in sorted(valid_fields, key=lambda x: len(valid_fields[x])):
    field = next(iter(valid_fields[i]))
    for k in valid_fields:
        if i != k:
            valid_fields[k].discard(field)

ans = 1
for col in valid_fields:
    field = valid_fields[col].pop()
    if 'departure' in field:
        ans *= your_ticket[col]

print('Part two answer: ', ans)
