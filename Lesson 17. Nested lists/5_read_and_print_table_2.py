row = int(input())
col = int(input())
table = [[input() for i in range(col)] for i in range(row)]
for i in range(row):
    print('\t'.join(table[i]))
print()
for i in range(col):
    print('\t'.join([table[j][i] for j in range(row)]))
