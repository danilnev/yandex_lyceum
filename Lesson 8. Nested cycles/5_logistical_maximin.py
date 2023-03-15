num = int(input())
minn = 0
for i in range(num):
    num2 = int(input())
    count_min = 0
    for j in range(num2):
        height = int(input())
        if height < count_min or count_min == 0:
            count_min = height
    if count_min > minn:
        minn = count_min
        count = i + 1
print(count, minn)