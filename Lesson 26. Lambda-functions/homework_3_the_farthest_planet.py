def find_farthest_orbit(list_of_orbits):
    list_of_orbits = list(filter(lambda x: x[0] != x[1], list_of_orbits))
    areas = list(map(lambda x: x[0] * x[1], list_of_orbits))
    return list_of_orbits[areas.index(max(areas))]


orbits = [(10, 10), (1, 100)]
print(*find_farthest_orbit(orbits))
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
