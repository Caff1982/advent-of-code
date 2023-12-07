from collections import Counter
from functools import cmp_to_key

CARD_TO_VALUE1 = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'J': 10,
    'Q': 11,
    'K': 12,
    'A': 13
}
CARD_TO_VALUE2 = {
    'J': 0,
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'Q': 10,
    'K': 11,
    'A': 12
}


def calculate_hand_values(hand, part_two):
    if part_two:
        num_jokers = hand['J']
        vals = sorted([v for k, v in hand.items() if k != 'J'], reverse=True)
        if num_jokers != 5:
            vals[0] += num_jokers
        else:
            vals = [0]
    else:
        vals = sorted(hand.values(), reverse=True)
    return vals


def compare_hands(card_to_value, part_two=False):
    def compare(item1, item2):
        (card_str1, bid1), hand1 = item1
        (card_str2, bid2), hand2 = item2

        vals1 = calculate_hand_values(hand1, part_two)
        vals2 = calculate_hand_values(hand2, part_two)

        # Check number of unique cards first
        if len(vals1) > len(vals2):
            return -1
        elif len(vals1) < len(vals2):
            return 1
        # Check value of highest card
        if max(vals1) < max(vals2):
            return -1
        elif max(vals1) > max(vals2):
            return 1
        # Check which hand has the highest card
        for i, j in zip(card_str1, card_str2):
            if card_to_value[i] < card_to_value[j]:
                return -1
            elif card_to_value[i] > card_to_value[j]:
                return 1
        return 0
    return compare


def calculate_total(hand_dict, compare_hands):
    total = 0
    for i, (k, v) in enumerate(sorted(hand_dict.items(), key=cmp_to_key(compare_hands)), start=1):
        total += i * k[1]
    return total


with open('inputs/input_day7.txt', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

hand_dict = {}
for line in lines:
    cards, bid = line.split()
    bid = int(bid)
    counter = Counter(cards)
    hand_dict[(cards, bid)] = counter

total1 = calculate_total(hand_dict, compare_hands(CARD_TO_VALUE1))
print(total1)
total2 = calculate_total(hand_dict, compare_hands(CARD_TO_VALUE2, part_two=True))
print(total2)
