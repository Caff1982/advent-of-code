from collections import deque


with open('day9.txt') as f:
    arr = list(map(int, f.read().splitlines()))


def is_valid(num_buffer, target):
    for i in num_buffer:
        for j in num_buffer:
            if i + j == target:
                return True
    return False

num_buffer = deque(arr[:25])
for i in range(25, len(arr)):
    if not is_valid(num_buffer, arr[i]):
        part1_ans = arr[i]
        print(part1_ans)
        break

    num_buffer.popleft()
    num_buffer.append(arr[i])


### Part Two ###

k = 2
running = True
while running:
    for i in range(len(arr)-k):
        if sum(arr[i:i+k]) == part1_ans:
            cont_set = arr[i:i+k]
            running = False
            print(min(cont_set) + max(cont_set))
    k += 1
