import numpy as np


def super_sort(rows, cols):
    a = np.random.randint(1, 100, (rows, cols))
    b = a.copy()
    b = np.rot90(b)
    if cols % 2 == 0:
        b[1::2].sort(axis=1)
    else:
        b[::2].sort(axis=1)
    b = np.rot90(b)
    b = np.rot90(b)
    b[1::2].sort(axis=1)
    b = np.rot90(b)
    return a, b


# print(super_sort(4, 4))
