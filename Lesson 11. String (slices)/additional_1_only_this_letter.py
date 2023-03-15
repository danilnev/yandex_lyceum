word = input()
num = int(input())
favorite = input()
if not (0 <= num - 1 < len(word)) or len(favorite) != 1:
    print('ОШИБКА')
elif word[num - 1] == favorite:
    print('ДА')
else:
    print('НЕТ')