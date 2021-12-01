

def is_valid(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for item in passport.split():
        key = item.split(':')[0][:3]
        if key != 'cid':
            required_fields.remove(item.split(':')[0][:3])
    return len(required_fields) == 0



valid_passports = []
passport = ''
with open('day4.txt') as f:
    for line in f.read().splitlines():
        if line == '':
            if is_valid(passport):
                valid_passports.append(passport)
            passport = ''
        else:
            passport += ' ' + line

if is_valid(passport):
    valid_passports.append(passport)

print(len(valid_passports))


### Part two ###
def is_valid_item(item):
    field, value = item.split(':')
    hex_chars = '0123456789abcdef'
    if field == 'byr':
        if not 1920 <= int(value) <= 2002:
            return False
    elif field == 'iyr':
        if not 2010 <= int(value) <= 2020:
            return False
    elif field == 'eyr':
        if not 2020 <= int(value) <= 2030:
            return False
    elif field == 'hgt':
        if value[-2:] not in ('cm', 'in'):
            return False
        if value[-2:] == 'cm' and not 150 <= int(value[:-2]) <= 193:
            return False
        elif value[-2:] == 'in' and not 59 <= int(value[:-2]) <= 76:
            return False
    elif field == 'hcl':
        if len(value) != 7:
            return False
        elif value[0] != '#':
            return False
        elif not all([i in hex_chars for i in value[1:]]):
            return False
    elif field == 'ecl':
        if value not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            return False
    elif field == 'pid':
        if len(value) != 9:
            return False
        elif not value.isdigit():
            return False
    return True

valid = 0
for passport in valid_passports:
    if all([is_valid_item(i) for i in passport.split()]):
        valid += 1

print(valid)
