from collections import defaultdict


nums = [0,8,15,2,12,1,4]

num_dict = defaultdict(list)
current_n = None
turn = 1
for n in nums:
    num_dict[n].append(turn)
    current_n = n
    turn += 1

while turn <= 30000000:
    if len(num_dict[current_n]) <= 1:
        num_dict[0].append(turn)
        current_n = 0
    else:
        diff = num_dict[current_n][-1] - num_dict[current_n][-2]
        current_n = diff
        num_dict[current_n].append(turn)
    
    if turn == 2020:
        # Part One answer
        print(current_n)
    
    turn += 1

print(current_n)
    