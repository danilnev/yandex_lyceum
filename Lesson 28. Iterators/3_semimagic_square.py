import sys


table = list(list(map(int, string.split())) for string in sys.stdin.readlines())
row_sums = list(map(sum, table))
col_sums = list(map(sum, zip(*table)))
if all(map(lambda x: x == row_sums[0], row_sums + col_sums)):
    print('YES')
else:
    print('NO')
