import re

with open("inputs/input_day13.txt", "r") as f:
    lines = f.readlines()


def solve(a_x, a_y, b_x, b_y, prize_x, prize_y):
    """
    We have two equations:
    a_x * A + b_x * B = prize_x
    a_y * A + b_y * B = prize_y

    This is a system of linear equations, which can be solved by
    elimination. We can solve for A by multiplying the first equation
    by b_y and the second by b_x and subtracting the two equations.
    We can then solve for B by substituting A into the first equation.
    """
    a = (prize_x * b_y - prize_y * b_x) / (a_x * b_y - a_y * b_x)
    b = (prize_x - a * a_x) / b_x
    return a, b

def parse_line(line, pattern):
    matches = re.search(pattern, line)
    return int(matches.group(1)), int(matches.group(2))

ab_pattern = r'X\+(\d+), Y\+(\d+)'
prize_pattern = r'X=(\d+), Y=(\d+)'
p2_amount = 10000000000000
total_p1 = 0
total_p2 = 0
for i in range(len(lines) // 4 + 1):
    a_x, a_y = parse_line(lines[i * 4], ab_pattern)
    b_x, b_y = parse_line(lines[i * 4 + 1], ab_pattern)
    prize_x, prize_y = parse_line(lines[i * 4 + 2], prize_pattern)

    a, b = solve(a_x, a_y, b_x, b_y, prize_x, prize_y)
    if int(a) == a and int(b) == b:
        total_p1 += a * 3 + b

    a, b = solve(a_x, a_y, b_x, b_y, prize_x + p2_amount, prize_y + p2_amount)
    if int(a) == a and int(b) == b:
        total_p2 += a * 3 + b

print(int(total_p1))
print(int(total_p2))
