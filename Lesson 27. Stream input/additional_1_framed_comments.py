import sys


data = list(map(str.strip, sys.stdin))
print('\n'.join(map(lambda x: f'Line {data.index(x) + 1}: {x[1:].strip()}', filter(lambda x: x.startswith('#'), data))))
