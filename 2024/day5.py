from collections import defaultdict


with open("inputs/input_day5.txt", "r") as f:
    lines = f.read()

rules, updates = lines.split("\n\n")
rule_dict = defaultdict(set)
for rule in rules.splitlines():
    a, b = map(int, rule.split("|"))
    rule_dict[b].add(a)
updates = [list(map(int, update.split(','))) for update in updates.splitlines()]

def is_valid(update):
    for i, num in enumerate(update):
        if num in rule_dict and rule_dict[num] & set(update[i:]):
            return False
    return True

def create_valid_update(update, rule_dict):
    i = 0
    while i < len(update):
        num = update[i]
        if num in rule_dict:
            for replacement in rule_dict[num]:
                if replacement in update[i:]:
                    swap_idx = update[i:].index(replacement) + i
                    update[i], update[swap_idx] = replacement, num
                    i = -1
                    break
        i += 1
    return update


p1_total = 0
p2_total = 0
for update in updates:
    if is_valid(update):
        p1_total += update[len(update) // 2]
    else:
        valid_update = create_valid_update(update, rule_dict)
        p2_total += valid_update[len(valid_update) // 2]

print(p1_total)
print(p2_total)