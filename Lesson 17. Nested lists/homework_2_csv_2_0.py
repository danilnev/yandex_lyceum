rows = int(input())
table = []
for i in range(rows):
    table.append(input().split(','))
num = int(input())
for i in range(num):
    crds = input().split(',')
    crd1 = int(crds[0])
    crd2 = int(crds[1])
    print(table[crd1][crd2])
