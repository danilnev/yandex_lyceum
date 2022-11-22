string1 = input()
num = ''
for i in range(4):
    if string1[i] != ' ':
        num += string1[i]
num = int(num)
summ1 = int(string1[4:])
sums = list()
indexes = list()
for i in range(num):
    string2 = input()
    price = ''
    n = ''
    summ2 = ''
    for j in range(7):
        if string2[j] != ' ':
            price += string2[j]
    for j in range(8, 12):
        if string2[j] != ' ':
            n += string2[j]
    for j in range(13, len(string2)):
        summ2 += string2[j]
    price = int(price)
    n = int(n)
    summ2 = int(summ2)
    sums.append(price * n)
    if price * n != summ2:
        indexes.append(i + 1)
result_summ = 0
for summ in sums:
    result_summ += summ
print(summ1 - result_summ)
for index in indexes:
    print(index, end=' ')
