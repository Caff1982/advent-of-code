

with open('day19.txt') as f:
    rules, messages = f.read().split('\n\n')
    rules = rules.splitlines()
    messages = messages.splitlines()


rule_dict = {}
for rule in rules:
    idx, contents = rule.split(': ')
    rule_dict[int(idx)] = contents


def solve(message, idx):
    rule = rule_dict[idx]
    if rule.startswith('"'):
        rule = rule.replace('"', '')
        if message.startswith(rule):
            return len(rule)
        else:
            return -1

    for option in rule.split(' | '):
        count = 0
        for rule_number in option.split():
            rn = int(rule_number)
            ret = solve(message[count:], rn)
            if ret == -1:
                count = -1
                break
            else:
                count += ret

        if count != -1:
            return count
    return -1


ans = 0
for message in messages:
    ret = solve(message, 0)
    if ret == len(message):
        ans += 1
print(ans)


### Part Two ###
rule_dict[8] = '42 | 42 8'
rule_dict[11] = '42 31 | 42 11 31'

def solve(message, idx):
    rule = rule_dict[idx]
    if rule.startswith('"'):
        rule = rule.replace('"', '')
        if message.startswith(rule):
            return [len(rule)]
        else:
            return []

    result = []
    for option in rule.split(' | '):
        count = [0]
        for rule_number in option.split():
            temp = []
            rn = int(rule_number)
            for i in count:
                ret = solve(message[i:], rn)
                for c in ret:
                    temp.append(c + i)
            count = temp
        result += count
    return result


ans = 0
for message in messages:
    ret = solve(message, 0)
    if len(message) in ret:
        ans += 1
print(ans)
