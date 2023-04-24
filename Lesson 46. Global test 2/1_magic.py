import sys


strings = list(map(str.rstrip, sys.stdin.readlines()))
strings = sorted(list(map(lambda y: ' '.join(list(map(lambda x: x[:3], y.split()))), strings)))
print(*strings, sep='\n')
