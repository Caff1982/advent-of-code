

with open('day22.txt') as f:
    p1, p2 = f.read().split('\n\n')
    p1 = list(map(int, p1[10:].split('\n')))
    p2 = list(map(int, p2[10:].split('\n')))


i = 1
while len(p1) > 0 and len(p2) > 0:
    i += 1
    print(i, p1, p2)
    a, b = p1.pop(0), p2.pop(0)
    if a > b:
        p1.extend([a, b])
    elif b > a:
        p2.extend([b, a])

winner = p1 if len(p1) > 0 else p2

ans = 0
for i, n in enumerate(winner):
    ans += (len(winner)-i) * n

print(ans)


### Part Two ###

def play_game(p1, p2):
    states = set()
    while len(p1) > 0 and len(p2) > 0:
        state = (tuple(p1), tuple(p2))
        if state in states:
            return 1, p1

        states.add(state)
        a = p1.pop(0)
        b = p2.pop(0)
        if len(p1) >= a and len(p2) >= b:
            result, hand = play_game(list(p1[:a]), list(p2[:b]))
            winner = p1 if result == 1 else p2
        else:
            if a > b:
                winner = p1
            elif b > a:
                winner = p2
            else:
                print('A equal to B')

        if winner == p1:
            p1.extend([a, b])
        else:
            p2.extend([b, a])

    return 1 if winner == p1 else 2, winner


with open('day22.txt') as f:
    p1, p2 = f.read().split('\n\n')
    p1 = list(map(int, p1[10:].split('\n')))
    p2 = list(map(int, p2[10:].split('\n')))

res, hand = play_game(p1, p2)
# print(res, hand)

ans = 0
for i, n in enumerate(hand):
    ans += (len(hand)-i) * n
print(ans)