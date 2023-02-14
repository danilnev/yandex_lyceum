import itertools
import sys


money = list(map(str.rstrip, sys.stdin.readlines()))
data = list(map(lambda x: x[:-1], filter(lambda x: len(x) > 1, map(lambda x: list(x[1]),
                                                                   itertools.groupby(sorted(money))))))
print(sum(map(lambda x: sum(map(lambda y: int(y.split()[0]), x)), data)))
