from collections import Counter


with open("inputs/input_day11.txt") as f:
    stones = f.read()

stones = list(map(int, stones.split()))
stones = Counter(stones)

n_steps = 75
for step in range(n_steps):
    if step == 25:
        print("Part 1: ", sum(new_stones.values()))
    new_stones = Counter()
    for stone, count in stones.items():
        stone_str = str(stone)
        stone_len = len(stone_str)
        if stone == 0:
            new_stones[1] += count
        elif stone_len % 2 == 0:
            mid = stone_len // 2
            a, b = stone_str[:mid], stone_str[mid:]
            new_stones[int(a)] += count
            new_stones[int(b)] += count
        else:
            new_stones[stone * 2024] += count
        
    stones = new_stones
    
print("Part 2: ", sum(new_stones.values()))