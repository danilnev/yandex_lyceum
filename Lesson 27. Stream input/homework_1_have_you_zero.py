import sys


print(any([str.rstrip('\n').split().count('0') for str in sys.stdin.readlines()]))
