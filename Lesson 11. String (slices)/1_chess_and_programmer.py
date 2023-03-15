size = int(input())
for i in range(size, 0, -1):
    for j in range(65, 65 + size):
        print(chr(j), i, sep='', end=' ')
    print()