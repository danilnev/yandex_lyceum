result = 'НЕТ'
n = int(input())
for i in range(n):
    string = input()
    if 'кот' in string or 'Кот' in string:
        result = 'МЯУ'
    if 'пёс' in string or 'Пёс' in string:
        result = 'НЕТ'
print(result)