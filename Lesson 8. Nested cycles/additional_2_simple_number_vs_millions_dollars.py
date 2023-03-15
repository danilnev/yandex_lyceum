num = int(input())
for i in range(2, num):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count <= 2:
        print(i)