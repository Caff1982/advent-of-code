import numpy as np


with open('input_day4.txt') as f:
    lines = f.read().splitlines()

nums = list(map(int, lines[0].split(',')))

squares = []
for i in range(2, len(lines), 6):
    squares.append([[int(j) for j in l.split()] for l in lines[i:i+5]])
squares = np.array(squares)

def solve(square, nums):
    card = np.zeros((5,5))
    for j, n in enumerate(nums):
        card[square == n] = True
        if any(np.sum(card, axis=0) == 5) or any(np.sum(card, axis=1) == 5):
            sq_sum = np.sum(np.where(card == False, square, 0))
            return [j, n * sq_sum]

# Part One
results = np.array([solve(square, nums) for square in squares])
print(results[np.argmin(results[:, 0])][1])


# Part Two
print(results[np.argmax(results[:, 0])][1])