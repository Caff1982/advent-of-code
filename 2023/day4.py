
with open('inputs/input_day4.txt', 'r') as f:
    lines = f.read().splitlines()


def parse_line(line):
    """Parse a line from the input file into sets of
    winning numbers and our numbers."""
    winning_nums, our_nums = line.split(':')[1].split('|')
    winning_nums = {int(num) for num in winning_nums.split()}
    our_nums = {int(num) for num in our_nums.split()}
    return winning_nums, our_nums


total = 0
for line in lines:
    winning_nums, our_nums = parse_line(line)
    n_matches = len(winning_nums & our_nums)
    if n_matches > 0:
        total += 2**(n_matches-1)

print(total)


# Part 2

n_cards = [1] * len(lines)
for i, line in enumerate(lines):
    winning_nums, our_nums = line.split(':')[1].split('|')
    winning_nums = {int(num) for num in winning_nums.split()}
    our_nums = {int(num) for num in our_nums.split()}
    n_matches = len(winning_nums & our_nums)

    if n_matches > 0:
        n_cards[i+1:i+n_matches+1] = [c + n_cards[i] for c in n_cards[i+1:i+n_matches+1]]

print(sum(n_cards))
