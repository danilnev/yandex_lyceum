number = int(input())
n = int(input())
lists = [number]
for i in range(n - 1):
    num10 = lists[i]
    num2 = ''
    while num10 > 0:
        num2 = str(num10 % 2) + num2
        num10 //= 2

    count10 = 0
    for val in num2:
        if val == '1':
            count10 += 1
    count2 = ''
    while count10 > 0:
        count2 = str(count10 % 2) + count2
        count10 //= 2
    last_num = num2 + count2
    num10 = 0
    lenn = len(last_num)
    for j in range(lenn):
        num10 += int(last_num[j]) * (2 ** (lenn - j - 1))
    lists.append(num10)
print(lists[-1])
