

with open("inputs/input_day7.txt") as f:
    lines = f.read().splitlines()


def is_valid(target, nums, part_two=False, memo=None):
    if memo is None:
        memo = {}

    def recurse(remaining_nums, current_sum):
        if not remaining_nums:
            return current_sum == target
        
        key = (tuple(remaining_nums), current_sum)
        if key in memo:
            return memo[key]

        next_num = remaining_nums[0]
        rest_nums = remaining_nums[1:]

        if recurse(rest_nums, current_sum + next_num):
            memo[key] = True
            return True
        if recurse(rest_nums, current_sum * next_num):
            memo[key] = True
            return True
        if part_two and recurse(rest_nums, int(str(current_sum) + str(next_num))):
            memo[key] = True
            return True

        memo[key] = False
        return False

    first_num = nums[0]
    return recurse(nums[1:], first_num)


total_p1 = 0
total_p2 = 0
for line in lines:
    target, nums = line.split(": ")
    target = int(target)
    nums = list(map(int, nums.split()))

    if is_valid(target, nums):
        total_p1 += target
    
    if is_valid(target, nums, part_two=True):
        total_p2 += target

print(total_p1)
print(total_p2)