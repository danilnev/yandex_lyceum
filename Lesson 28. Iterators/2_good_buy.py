import sys


books = input().strip().split('\t')
data = list(map(lambda x: x.rstrip().split('\t'), sys.stdin.readlines()))
data = list(map(lambda x: [x[0]] + list(map(int, x[1:])), data))
good_price = min(data, key=lambda x: x[1:])
print(good_price[0])
print('\n'.join([f'{mag}\t{price}' for mag, price in zip(books, good_price[1:])]))
