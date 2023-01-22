def fac(num: int) -> int:
    multiply = 1
    for i in range(1, num + 1):
        multiply *= i
    return multiply


def catalan(n: int) -> int:
    return fac(2 * (n)) / (fac(n + 1) * fac(n))


# print(fac(3))
# print(fac(4))
# print(fac(6))
# print(catalan(0))
# print(catalan(1))
# print(catalan(2))
# print(catalan(3))
