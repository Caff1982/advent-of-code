import re


def replace_string_digits(text):
    number_dict = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': 'f4r',
        'five': 'f5e',
        'six': 's6x',
        'seven': 's7n',
        'eight': 'e8t',
        'nine': 'n9e'
    }
    for key, value in number_dict.items():
        text = text.replace(key, value)

    return text


def solve(lines):
    total = 0
    for line in lines:
        a = re.search('\d', line)
        b = re.search('\d(?=[^\d]*$)', line)

        total += int(a.group() + b.group())

    print(total)


if __name__ == "__main__":
    with open('inputs/input_day1.txt', 'r') as f:
        text = f.read()

    # Part 1
    solve(text.splitlines())

    # Part 2
    solve(replace_string_digits(text).splitlines())
