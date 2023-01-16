def triangle(a, b, c):
    array = [a, b, c]
    if (array.pop(array.index(min(array))) + min(array)) > max(array):
        print('Это треугольник')
    else:
        print('Это не треугольник')


# triangle(1, 1, 2)
# triangle(7, 6, 10)
# triangle(20, 13, 17)
