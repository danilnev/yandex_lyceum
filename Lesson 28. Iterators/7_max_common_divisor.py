import functools
import sys
import math


numbers = list(map(lambda x: int(x.rstrip()), sys.stdin))
print(functools.reduce(lambda a, b: math.gcd(a, b), numbers))
