import sys


data = sys.stdin.readlines()
print(len(list(filter(lambda x: x.lstrip().startswith('#'), data))))
