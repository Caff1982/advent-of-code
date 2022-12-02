

with open('inputs/input_day2.txt') as f:
    lines = f.read().splitlines()

score_dict = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
    'C Z': 6
}
score = sum([score_dict[line] for line in lines])
print('Part one: ', score)

score_dict2 = {
    'A X': 3,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
    'C Z': 7
}
score = sum([score_dict2[line] for line in lines])
print('Part two: ', score)
