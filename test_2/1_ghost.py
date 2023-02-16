import sys


data = list(map(lambda x: list(map(int, x.split('+'))), sys.stdin.readlines()))
data = list(map(lambda x: list(filter(lambda y: y % 10 == 0, x)), data))
print(*map(str, max(data, key=lambda x: len(x))))
