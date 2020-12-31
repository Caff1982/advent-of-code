import re

parens_match = r'\(([0-9]|\*|\+|\s)*\)'

test_str1 = '1 + 2 * 3 + 4 * 5 + 6'
test_str2 = '1 + (2 * 3) + (4 * (5 + 6))'

def evaluate(expression):
    expression = expression.split()
    ans = int(expression[0])
    for i, char in enumerate(expression[1:]):
        if char == '+':
            ans += int(expression[i+2])
        elif char == '*':
            ans *= int(expression[i+2])

    return ans


def solve(line):
    match = re.search(parens_match, line)
    if match:
        start, end = match.span()
        return solve(line[:start] + str(evaluate(match.group()[1:-1])) + line[end:])
    return evaluate(line)


ans = 0
with open('day18.txt') as f:
    for line in f.read().splitlines():
        ans += solve(line)
print(ans)


### Part Two ###

class Num(int):

    def __add__(self, other):
        return Num(super().__mul__(other))

    def __mul__(self, other):
        return Num(super().__add__(other))


def solve(line):
    match = re.search(parens_match, line)
    if match:
        start, end = match.span()
        return solve(line[:start] + str(eval(match.group()[1:-1])) + line[end:])
    return evaluate(line)


ans = 0
with open('day18.txt') as f:
    for line in f.read().splitlines():
        new_line = []
        for char in line:
            if char == '+':
                new_line.append('*')
            elif char == '*':
                new_line.append('+')
            elif char in '() ':
                new_line.append(char)
            else:
                new_line.append(f'Num({char})')

        ans += eval(''.join(new_line))

print(ans)