num = int(input())
table = [[0] * num] * num
max_way = 0
for i in range(1, num):
    row = [int(num) for num in input().split()]
    table[i] = row
    for j in range(num - len(row)):
        table[i].append(0)
for i in range(num - 1):
    for j in range(i + 1, num):
        table[i][j] = table[j][i]
a, b = [int(num) for num in input().split()]
for i in range(num):
    fromm = table[a][i]
    to = table[i][b]
    if a != i and (max_way == 0 or fromm + to < max_way[1]):
        max_way = (j, fromm + to)
without_way = table[a][b]
if max_way[1] < without_way:
    print(max_way[0])
else:
    print(a)
