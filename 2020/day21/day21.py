from collections import defaultdict

allergy_dict = {}
counter = defaultdict(int)
with open('day21.txt') as f:
    for line in f.read().splitlines():
        ingredients, allergies = line.split('(contains')
        ingredients = ingredients.split()
        allergies = allergies[:-1].split(',')
        for a in allergies:
            if a in allergy_dict:
                allergy_dict[a] &= set(ingredients)
            else:
                allergy_dict[a] = set(ingredients)

        for i in ingredients:
            counter[i] += 1

ans = 0
for i, count in counter.items():
    if all([i not in v for v in allergy_dict.values()]):
        ans += count

print(ans)


### Part Two ###

ans = {}
while len(ans) < len(allergy_dict):
    for allergy, ingredients in allergy_dict.items():
        if len(ingredients) == 1:
            ingredient = ingredients.pop()
            ans[allergy] = ingredient
            for vals in allergy_dict.values():
                vals.discard(ingredient)


print(','.join(i[1] for i in sorted(ans.items(), key=lambda x: x[0])))


