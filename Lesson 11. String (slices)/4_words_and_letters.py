maxx = ''
minn = ''
result = 'ДА'
while True:
    word = input()
    if word == 'стоп':
        break
    elif len(word) > len(maxx):
        maxx = word
    elif len(word) < len(minn) or minn == '':
        minn = word
for letter in minn:
    if letter not in maxx:
        result = 'НЕТ'
print(result)