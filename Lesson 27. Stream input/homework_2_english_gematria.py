import sys

data = list(map(str.rstrip, sys.stdin))
data.sort(key=lambda x: (sum([ord(el) - ord('A') + 1 for el in x.upper()]), x))
print('\n'.join(data))
