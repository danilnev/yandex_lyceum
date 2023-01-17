def tic_tac_toe(field):
    count_x = False
    count_zeros = False
    winner = None
    for i in range(3):
        if field[i] == ['x', 'x', 'x'] or [field[j][i] for j in range(3)] == ['x', 'x', 'x']:
            winner = 'x'
            count_x = True
        if field[i] == ['0', '0', '0'] or [field[j][i] for j in range(3)] == ['0', '0', '0']:
            winner = '0'
            count_zeros = True
    if [field[i][i] for i in range(3)] == ['x', 'x', 'x'] or [field[i][2 - i] for i in range(3)] == ['x', 'x', 'x']:
        winner = 'x'
        count_x = True
    if [field[i][i] for i in range(3)] == ['0', '0', '0'] or [field[i][2 - i] for i in range(3)] == ['0', '0', '0']:
        winner = '0'
        count_zeros = True
    if (count_x and not count_zeros) or (count_zeros and not count_x):
        print(f'{winner} win')
    else:
        print('draw')


# data = """0 - 0
# x x x
# 0 0 -"""
#
# field = [line.split() for line in data.split('\n')]
# tic_tac_toe(field)

# data="""x 0 -
# x - 0
# x 0 -"""
#
# field = [line.split() for line in data.split('\n')]
# tic_tac_toe(field)
