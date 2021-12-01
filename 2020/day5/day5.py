
with  open('day5.txt') as f:
    passes = f.read().splitlines()

seat_ids = []
for p in passes:
    # Convert to binary
    row_bin = p[:7].replace('B', '1').replace('F', '0')
    col_bin = p[7:].replace('R', '1').replace('L', '0')
    row = int(row_bin, 2)
    col = int(col_bin, 2)
    seat_ids.append((row * 8) + col)

print(max(seat_ids))


### Part Two ###
seat_ids = sorted(seat_ids)
for i in range(1, len(seat_ids)):
    if seat_ids[i] - seat_ids[i-1] != 1:
        print(seat_ids[i] - 1)
        break