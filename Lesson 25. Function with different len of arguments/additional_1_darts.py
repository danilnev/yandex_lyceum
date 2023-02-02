def score(place, sector=None):
    if place in list(scoring.keys())[:2]:
        return scoring[place]
    else:
        return scoring[place][sector]


scoring = {
    'Яблочко': 50,
    'Зеленоек_кольцо': 25,
    'Внешнее_кольцо': {1: 8, 2: 6, 3: 42},
    'Внутреннее_кольцо': {1: 2, 2: 9, 3: 56}
}
print(score("Яблочко"))
print(score("Внешнее_кольцо", 1))