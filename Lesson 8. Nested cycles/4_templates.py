begin = int(input())
finall = int(input())
step = int(input())
for i in range(begin, finall + 1, step):
    for j in range(begin, finall + 1, step):
        print(i, '+', j, '=', i + j, end='\t')
    print()
