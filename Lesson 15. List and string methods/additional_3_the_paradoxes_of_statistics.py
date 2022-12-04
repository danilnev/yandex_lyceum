num_numbers = int(input())
groups = [[int(number) for number in input().split()] for i in range(num_numbers)]
medians = []
mods = []
all_numbers = []
for i in range(num_numbers):
    group = groups[i]

    group.sort()
    medians.append(str(group[len(group) // 2]))

    max_count = 0
    for number in group:
        if max_count == 0:
            value = str(number)
            max_count = group.count(number)
        elif group.count(number) > max_count:
            value = str(number)
            max_count = group.count(number)
        all_numbers.append(number)
    mods.append(value)
print(' '.join(medians), ' '.join(mods), sep='\n')
medians.sort()
all_numbers.sort()
max_count = 0
for mod in mods:
    if mods.count(mod) > max_count:
        max_count = mods.count(mod)
        max_mod = mod
max_count = 0
for number in all_numbers:
    if all_numbers.count(number) > max_count:
        max_count = all_numbers.count(number)
        max_all_mod = number
print(medians[len(medians) // 2],
      max_mod,
      all_numbers[len(all_numbers) // 2],
      max_all_mod,
      sep='\n')
