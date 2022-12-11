import numpy as np


class Monkey:

    def __init__(self, items, operation, divisor, actions):
        self.items = items
        self.operation = operation
        self.divisor = divisor
        self.actions = actions # (True, False)

        self.total_items = 0

    def update_total_items(self):
        self.total_items += len(self.items)



with open('inputs/input_day11.txt') as f:
    lines = f.read().splitlines()


def get_monkeys():
    monkeys = []
    for start_idx in range(0, len(lines), 7):
        items = list(map(int, lines[start_idx+1].split(': ')[1].split(',')))
        op = lines[start_idx+2].split(' = ')[1]
        operation = eval(f'lambda old: {op}')
        divisor = int(lines[start_idx+3].split()[-1])
        actions = (int(lines[start_idx+4].split()[-1]),
                   int(lines[start_idx+5].split()[-1]),)
        monkey = Monkey(items, operation, divisor, actions)
        monkeys.append(monkey)
    return monkeys

monkeys = get_monkeys()
for r in range(20):
    for m in monkeys:
        m.update_total_items()
        m.items = [m.operation(i) // 3 for i in m.items]
        for item in m.items:
            if item % m.divisor:
                monkeys[m.actions[1]].items.append(item)
            else:
                monkeys[m.actions[0]].items.append(item)
        m.items = []

total_items = sorted([m.total_items for m in monkeys])
# Part one answer
print(total_items[-2] * total_items[-1])



# Part two
monkeys = get_monkeys()
# Find the lowest common multiple to use for modulo
modulo = np.lcm.reduce([m.divisor for m in monkeys])
for r in range(10000):
    for m in monkeys:
        m.update_total_items()
        m.items = [m.operation(i) % modulo for i in m.items]
        for item in m.items:
            if item % m.divisor:
                monkeys[m.actions[1]].items.append(item)
            else:
                monkeys[m.actions[0]].items.append(item)
        m.items = []

total_items = sorted([m.total_items for m in monkeys])
print(total_items[-2] * total_items[-1])