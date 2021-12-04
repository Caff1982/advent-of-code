

with open('input_day3.txt') as f:
    lines = f.read().splitlines()

# Part One
gamma = ''
for i in range(len(lines[0])):
    bit_count = [lines[j][i] for j in range(len(lines))].count('1')
    gamma += '1' if bit_count > len(lines)//2 else '0'

epsilon = ''.join(['0' if i == '1' else '1' for i in gamma])

print(int(gamma, 2) * int(epsilon, 2))


# Part Two
gamma = lines.copy()
for i in range(len(lines[0])):
    bit_count = [gamma[j][i] for j in range(len(gamma))].count('1')
    if bit_count >= len(gamma) / 2:
        gamma = [line for line in gamma if line[i] == '1']
    else:
        gamma = [line for line in gamma if line[i] == '0']

    if len(gamma) == 1:
        # print(gamma[0])
        break

epsilon = lines.copy()
for i in range(len(lines[0])):
    bit_count = [epsilon[j][i] for j in range(len(epsilon))].count('1')
    if bit_count >= len(epsilon) / 2:
        epsilon = [line for line in epsilon if line[i] == '0']
    else:
        epsilon = [line for line in epsilon if line[i] == '1']

    if len(epsilon) == 1:
        # print(epsilon[0])
        break

print(int(gamma[0], 2) * int(epsilon[0], 2))
