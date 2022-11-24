num = int(input())
numbers = []
flag = False
for i in range(num):
    numbers.append(int(input()))
multiply = int(input())
for i in range(num):
    number = numbers[i]
    for j in range(num):
        if j != i and numbers[i] * numbers[j] == multiply:
            flag = True
            break
    if flag:
        break
if flag:
    print('ДА')
else:
    print('НЕТ')