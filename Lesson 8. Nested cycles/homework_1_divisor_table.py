y = int(input())
x = int(input())
for i in range(1, x + 1):
    for j in range(1, y + 1):
        print(j / i, end=' ')
    print()