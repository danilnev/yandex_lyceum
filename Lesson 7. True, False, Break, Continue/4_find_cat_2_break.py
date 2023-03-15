count = 0
result = -1
while True:
    string = input()
    if string == 'СТОП':
        break
    count += 1
    if 'кот' in string or 'Кот' in string:
        result = count
        break
print(result)