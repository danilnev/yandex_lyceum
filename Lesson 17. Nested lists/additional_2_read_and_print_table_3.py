rows = int(input())
cols = int(input())
table = [[input() for i in range(cols)] for i in range(rows)]
for row in table:
    print('\t'.join(row))
