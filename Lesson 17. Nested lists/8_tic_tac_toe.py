length = int(input())
table = []
flag = True
for i in range(length):
    table.append(list(input()))
for i in range(length):
    for j in range(len(table[i]) - 2):
        row = table[i][j:j + 3]
        if row == ['o'] * 3:
            print('o')
            flag = False
            break
        elif row == ['x'] * 3:
            print('x')
            flag = False
            break
    if not flag:
        break
if flag:
    for i in range(length - 2):
        for j in range(length):
            col = [table[k][j] for k in range(i, i + 3)]
            if col == ['o'] * 3:
                print('o')
                flag = False
                break
            elif col == ['x'] * 3:
                print('x')
                flag = False
                break
        if not flag:
            break
if flag:
    print('-')
