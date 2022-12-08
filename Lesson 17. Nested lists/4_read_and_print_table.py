row = int(input())
col = int(input())
table = [[input() for i in range(col)] for i in range(row)]
for row in table:
    print('\t'.join(row))
