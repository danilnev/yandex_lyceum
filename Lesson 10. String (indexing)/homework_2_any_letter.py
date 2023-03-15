word = input()
num = int(input()) - 1
if 0 <= num < len(word):
    print(word[num])
else:
    print('ОШИБКА')