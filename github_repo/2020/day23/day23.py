test_input = '389125467'
puzzle_input = '135468729'


def step(cups):
    removed_cups = cups[1:4]
    destination = cups[0] - 1
    if destination == 0:
        destination = max(cups)

    while destination in removed_cups:
        destination -= 1
        if destination == 0:
            destination = max(cups)



    idx = cups.index(destination)
    first_part = cups[:idx]
    return  first_part[4:] + [destination] + removed_cups + cups[idx+1:] + [cups[0]]


cups = list(map(int, puzzle_input))
for _ in range(100):
    cups = step(cups)

print(cups)
idx = cups.index(1)
print(''.join([str(i) for i in cups[idx+1:] + cups[:idx]]))


### Part Two ###

cups = list(map(int, puzzle_input))
cups += list(range(max(cups)+1, 1000001))

cups_dict = {num: cups[(idx+1)% len(cups)] for idx, num in enumerate(cups)}
current = cups[0]
max_val = max(cups)
i = 0
for move in range(10000000):
    i += 1
    if i % 500000 == 0:
        print(i)

    cup1 = cups_dict[current]
    cup2 = cups_dict[cup1]
    cup3 = cups_dict[cup2]
    next_cup = cups_dict[cup3]
    removed_cups = [cup1, cup2, cup3]

    destination = current -1
    if destination == 0:
        destination = max_val
    while destination in removed_cups:
        destination -= 1
        if destination == 0:
            destination = max_val

    cups_dict[current] = cups_dict[cup3]
    cups_dict[cup3] = cups_dict[destination]
    cups_dict[destination] = cup1

    current = next_cup


current = 1
final_arr = []
for cup in cups_dict:
    final_arr.append(current)
    current = cups_dict[current]

print(final_arr[1] * final_arr[2])