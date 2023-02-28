import random


def make_bingo():
    array = list(random.sample(range(1, 76), 25))
    array[12] = 0
    result = []
    for i in range(0, 21, 5):
        result.append(array[i:i + 5])
    return tuple(map(tuple, result))
