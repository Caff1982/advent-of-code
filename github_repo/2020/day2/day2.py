

with open('day2.txt', 'r') as f:
    arr = f.read().splitlines()

valid_passwords = 0
for line in arr:
    policy, password = line.split(':')
    letter = policy[-1]
    policy = policy[:-2] # Remove letter and space from end
    min_value, max_value = list(map(int, policy.split('-')))
    letter_count = password.count(letter)
    if min_value <= letter_count <= max_value:
        valid_passwords += 1

print(valid_passwords)


### Part Two ###
valid_passwords = 0
for line in arr:
    policy, password = line.split(':')
    password = password.strip() # Remove whitespace from password
    letter = policy[-1]
    policy = policy[:-2] # Remove letter and space from end
    pos_A, pos_B = list(map(int, policy.split('-')))
    # Zero-index positions
    pos_A -= 1
    pos_B -= 1
    if (password[pos_A] == letter) ^ (password[pos_B] == letter):
       valid_passwords += 1

print(valid_passwords)