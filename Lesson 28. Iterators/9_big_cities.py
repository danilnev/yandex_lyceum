import sys


data = list(map(lambda x: (x.split()[0], int(x.split()[2])), sys.stdin.readlines()))
data = list(map(lambda x: (x[0], f'{(x[1] // 100000) * 100} - {(x[1] // 100000) * 100 + 100}'), data))
cities = dict()
for city in data:
    if city[1] in cities:
        cities[city[1]].append(city[0])
    else:
        cities[city[1]] = [city[0]]
keys = sorted(cities.keys(), key=lambda x: int(x.split()[0]))
print('\n'.join(list(map(lambda x: f'{x}: {", ".join(sorted(cities[x]))}', keys))))
