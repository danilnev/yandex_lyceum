n = int(input())
word = 'НЕТ'
for i in range(n):
    string = input()
    if 'кот' in string or 'Кот' in string:
        word = 'МЯУ'
        break
print(word)