n = int(input())
count = 1
for i in range(1, n + 1):
    for j in range(i):
        print(count, end=' ')
        count += 1
        if count > n:
            break
    if count > n:
        break
    print()