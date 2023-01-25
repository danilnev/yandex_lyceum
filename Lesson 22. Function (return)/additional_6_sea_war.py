def read_field():
    return [list(input()) for i in range(4)]


def print_field(field):
    print('\n'.join([''.join(row) for row in field]))


def mirror_by_horizontally(field):
    mirror_field = [[' ' for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            mirror_field[i][-j - 1] = field[i][j]
    return mirror_field


def mirror_by_vertical(field):
    mirror_field = [[' ' for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            mirror_field[-i - 1][j] = field[i][j]
    return mirror_field


def transposition(field):
    transposition_field = [[' ' for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            transposition_field[j][i] = field[i][j]
    return transposition_field


one_field = read_field()
print_field(one_field)
print_field(mirror_by_horizontally(one_field))
print_field(mirror_by_vertical(one_field))
print_field(transposition(one_field))
print_field(mirror_by_vertical(mirror_by_horizontally(one_field)))
print_field(transposition(mirror_by_horizontally(one_field)))
print_field(transposition(mirror_by_vertical(one_field)))
print_field(transposition(mirror_by_vertical(mirror_by_horizontally(one_field))))
