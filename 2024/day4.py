

with open('inputs/input_day4.txt', 'r') as f:
    data = f.read().splitlines()


targets = ("XMAS", "SAMX")
n_rows = len(data)
n_cols = len(data[0])
p1_total = 0
p2_total = 0
for row in range(n_rows):
    for col in range(n_cols):
        if col + 3 < n_cols:
            if data[row][col:col + 4] in targets:
                p1_total += 1
        if row + 3 < n_rows:
            if data[row][col] + data[row + 1][col] + data[row + 2][col] + data[row + 3][col] in targets:
                p1_total += 1
        if row + 3 < n_rows and col + 3 < n_cols:
            if data[row][col] + data[row + 1][col + 1] + data[row + 2][col + 2] + data[row + 3][col + 3] in targets:
                p1_total += 1
            if data[row][col + 3] + data[row + 1][col + 2] + data[row + 2][col + 1] + data[row + 3][col] in targets:
                p1_total += 1
        
        if 1 <= row < n_rows -1 and 1 <= col < n_cols - 1:
            if data[row][col] == "A":
                if data[row - 1][col - 1] == "M" and data[row + 1][col - 1] == "M" and data[row - 1][col + 1] == "S" and data[row + 1][col + 1] == "S":
                    p2_total += 1
                elif data[row - 1][col - 1] == "S" and data[row + 1][col - 1] == "S" and data[row - 1][col + 1] == "M" and data[row + 1][col + 1] == "M":
                    p2_total += 1
                elif data[row - 1][col - 1] == "S" and data[row + 1][col - 1] == "M" and data[row - 1][col + 1] == "S" and data[row + 1][col + 1] == "M":
                    p2_total += 1
                elif data[row - 1][col - 1] == "M" and data[row + 1][col - 1] == "S" and data[row - 1][col + 1] == "M" and data[row + 1][col + 1] == "S":
                    p2_total += 1

print(p1_total)
print(p2_total)