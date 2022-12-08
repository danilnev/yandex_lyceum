rows = int(input())
table = [input().split(',') for i in range(rows)]
num = int(input())
for i in range(num):
    crd1, crd2 = [int(crd) for crd in input().split(',')]
    print(table[crd1][crd2])
