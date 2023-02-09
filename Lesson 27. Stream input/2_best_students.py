classes = int(input())
if all([any([input().split()[1] == '5' for j in range(int(input()))]) for i in range(classes)]):
    print('ДА')
else:
    print('НЕТ')
