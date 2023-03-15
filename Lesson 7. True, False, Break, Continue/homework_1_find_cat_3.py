result = -1
count = 0
count_cats = 0
while True:
    string = input()
    if string == 'СТОП':
        break
    count += 1
    if 'кот' in string or 'Кот' in string:
        count_cats += 1
        if result == -1:
            result = count
print(count_cats, result)