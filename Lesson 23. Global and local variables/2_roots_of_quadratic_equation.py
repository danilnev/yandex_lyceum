def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def larger_root(p, q):
    d = discriminant(1, p, q)
    return (- p + d ** 0.5) / 2


def smaller_root(p, q):
    d = discriminant(1, p, q)
    return (- p - d ** 0.5) / 2


def main():
    p = float(input())
    q = float(input())
    d = discriminant(1, p, q)
    print(d)
    print(smaller_root(p, q), larger_root(p, q))


# main()
