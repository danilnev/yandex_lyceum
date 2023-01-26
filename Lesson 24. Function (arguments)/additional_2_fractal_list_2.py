def defractalize(fractal):
    for el in fractal:
        if el == fractal:
            fractal.remove(el)


# fractal = [2, 5]
# fractal.append(fractal)
# fractal.append(3)
# fractal.append(fractal)
# fractal.append(9)
# defractalize(fractal)
# print(fractal)
