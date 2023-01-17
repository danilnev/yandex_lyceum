def squared(a, b, k):
    for i in range(a, b + 1, 10):
        row = []
        for j in range(i, i + 10):
            if (j ** 2) % k != 0 and j <= b:
                str_number = str(j ** 2)
                spaces = ' ' * (5 - len(str_number))
                row.append(str_number + spaces)
        print(''.join(row))


# squared(11, 99, 10)
# squared(4, 33, 9)
# squared(22, 64, 5)
# squared(3, 33, 14)
