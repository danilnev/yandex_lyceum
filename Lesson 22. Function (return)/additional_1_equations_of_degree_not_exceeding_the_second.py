def roots_of_quadratic_equation(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return ['all']
    elif a == 0 and b == 0:
        return []
    elif a == 0:
        return [0 - c / b]
    elif b == 0 and c == 0:
        return [0]
    elif b == 0:
        if (c / a) < 0:
            return []
        elif (c / a) > 0:
            return [(-c / a) ** 0.5, -(-c / a) ** 0.5]
    elif c == 0:
        return [0, -b / a]
    else:
        d = (b ** 2) - (4 * a * c)
        if d < 0:
            return []
        elif d == 0:
            return [-b / (2 * a)]
        elif d > 0:
            return [
                (-b + (d ** 0.5)) / (2 * a),
                (-b - (d ** 0.5)) / (2 * a)
            ]


result = roots_of_quadratic_equation(2, -8, 8)
print(result)
