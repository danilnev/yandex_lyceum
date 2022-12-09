num = int(input())
table = [[0] * num] * num
for i in range(1, num):
    row = [int(num) for num in input().split()]
    table[i] = row
    for j in range(num - len(row)):
        table[i].append(0)
for i in range(num - 1):
    for j in range(i + 1, num):
        table[i][j] = table[j][i]
for i in range(num):
    string = ''
    for j in range(num):
        string += str(table[i][j]) + ' '
    print(string.strip())
