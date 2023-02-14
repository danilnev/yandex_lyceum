import functools
import sys


words = list(map(str.rstrip, sys.stdin))
print(functools.reduce(lambda a, b: min(a, b), words))
