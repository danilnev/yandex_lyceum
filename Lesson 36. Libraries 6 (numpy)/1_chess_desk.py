import numpy as np


def make_field(size):
    array = np.zeros((size, size), dtype=np.int8)
    array[::2, ::2] = 1
    array[1::2, 1::2] = 1
    return array
