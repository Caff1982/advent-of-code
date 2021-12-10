from collections import Counter


with open('inputs/input_day10.txt') as f:
    lines = f.read().splitlines()


def check_line(line):
    """
    If line is corrupted it returns the invalid char.
    If line is incomplete it returns list of missing chars.
    """
    chunk_dict = {
        '}': '{',
        ')': '(',
        ']': '[',
        '>': '<'
    }
    stack = []
    for char in line:
        if char in '{([<':
            stack.append(char)
        else:
            if stack.pop() != chunk_dict[char]:
                return char
    return stack[::-1]

scores_p1 = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
scores_p2 = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4 
}
p1_score = 0
p2_scores = []
for l in lines:
    ret = check_line(l)
    if type(ret) == str:
        p1_score += scores_p1[ret]
    else:
        score = 0
        for i in ret:
            score *= 5
            score += scores_p2[i]
        p2_scores.append(score)

print('Part one: ', p1_score)
print('Part two: ', sorted(p2_scores)[len(p2_scores)//2])

