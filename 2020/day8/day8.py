
with open('day8.txt') as f:
    instructions = f.read().splitlines()


def run_instructions(instructions):
    idx = 0
    acc = 0
    visited = set()
    while True:
        if idx in visited:
            return False, acc
        elif idx >= len(instructions):
            return True, acc

        visited.add(idx)
        command, value = instructions[idx].split()
        if command == 'acc':
            acc += int(value)
            idx += 1
        elif command == 'nop':
            idx += 1
        else:
            idx += int(value)

_, acc = run_instructions(instructions)
print(acc)


### Part Two ###
for i in range(len(instructions)):
    if instructions[i].split()[0] == 'jmp':
        ins_copy = instructions[:]
        ins_copy[i] = ins_copy[i].replace('jmp', 'nop')
        success, acc = run_instructions(ins_copy)
        if success == True:
            print(acc)
            break
    elif instructions[i].split()[0] == 'nop':
        ins_copy = instructions[:]
        ins_copy[i] = ins_copy[i].replace('nop', 'jmp')
        success, acc = run_instructions(ins_copy)
        if success == True:
            print(acc)
            break
