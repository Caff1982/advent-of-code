

with open("inputs/input_day7.txt") as f:
    lines = f.read().splitlines()


def is_valid(target, nums, part_two=False):
    def recurse(remaining_nums, current_result):
        if not remaining_nums:
            return current_result == target
        
        next_num = remaining_nums[0]
        rest_nums = remaining_nums[1:]

        if recurse(rest_nums, current_result + next_num):
            return True
        if recurse(rest_nums, current_result * next_num):
            return True
        if part_two and recurse(rest_nums, int(str(current_result)  + str(next_num))):
            return True

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