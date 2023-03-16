import numpy as np


def snake(rows, cols):
    array = np.arange(1, rows * cols + 1).reshape(rows, cols)
    array[1::2] = array[1::2, ::-1]
    return array
