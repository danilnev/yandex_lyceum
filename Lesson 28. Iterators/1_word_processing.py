import sys


text = list(map(lambda x: x[:-1] if not x.isalpha() else x, sys.stdin.read().split()))
data = set((filter(lambda x: x.istitle(), text)))
print('\n'.join(map(lambda x: f'{text.index(x)} - {x}', sorted(list(data)))))

