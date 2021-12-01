import numpy as np


DIRECTIONS = ((0, 1), (0, -1), (1, 1), (1, -1),
              (-1, 1), (-1, -1), (1, 0), (-1, 0))

def step(matrix):
    new_matrix = []
    for row in range(len(matrix)):
        temp_row = ''
        for col in range(len(matrix[0])):
            neighbours = []
            for delta_y, delta_x in DIRECTIONS:
                y = row + delta_y
                x = col + delta_x
                if 0 <= y < len(matrix) and 0 <= x < len(matrix[0]):
                    neighbours.append(matrix[y][x])
            if matrix[row][col] == 'L' and '#' not in neighbours:
                temp_row += '#'
            elif matrix[row][col] == '#' and neighbours.count('#') >= 4:
                temp_row += 'L'
            else:
                temp_row += matrix[row][col]
        new_matrix.append(temp_row)

    return new_matrix


with open('day11.txt') as f:
    matrix = f.read().splitlines()

while True:
    new_matrix = step(matrix)
    if new_matrix == matrix:
        print(sum([row.count('#') for row in new_matrix]))
        break
    else:
        matrix = new_matrix


### Part Two ###

def step(matrix):
    new_matrix = []
    for row in range(len(matrix)):
        temp_row = ''
        for col in range(len(matrix[0])):
            neighbours = []
            for dy, dx in DIRECTIONS:
                i = 1
                while 0 <= row+dy*i < len(matrix) and 0 <= col+dx*i < len(matrix[0]):
                    if matrix[row+dy*i][col+dx*i] != '.':
                        neighbours.append(matrix[row+dy*i][col+dx*i])
                        break
                    i += 1

            if matrix[row][col] == 'L' and '#' not in neighbours:
                temp_row += '#'
            elif matrix[row][col] == '#' and neighbours.count('#') >= 5:
                temp_row += 'L'
            else:
                temp_row += matrix[row][col]
        new_matrix.append(temp_row)
        
    return new_matrix

with open('day11.txt') as f:
    matrix = f.read().splitlines()

while True:
    # for row in matrix:
    #     print(row)
    # print('\n')
    new_matrix = step(matrix)
    if new_matrix == matrix:
        print(sum([row.count('#') for row in new_matrix]))
        break
    else:
        matrix = new_matrix

