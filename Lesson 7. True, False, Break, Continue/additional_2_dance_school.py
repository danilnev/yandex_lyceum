num = int(input())
error_count = 0
count = 0
while True:
    string = input()
    if string == 'раз':
        count += 1
    else:
        print('Правильных отсчётов было ', count, ', но теперь вы ошиблись.', sep='')
        count = 0
        error_count += 1
        if error_count == num:
            print('На сегодня хватит.')
            break
        continue
    string = input()
    if string == 'два':
        count += 1
    else:
        print('Правильных отсчётов было ', count, ', но теперь вы ошиблись.', sep='')
        count = 0
        error_count += 1
        if error_count == num:
            print('На сегодня хватит.')
            break
        continue
    string = input()
    if string == 'три':
        count += 1
    else:
        print('Правильных отсчётов было ', count, ', но теперь вы ошиблись.', sep='')
        count = 0
        error_count += 1
        if error_count == num:
            print('На сегодня хватит.')
            break
        continue
    string = input()
    if string == 'четыре':
        count += 1
    else:
        print('Правильных отсчётов было ', count, ', но теперь вы ошиблись.', sep='')
        count = 0
        error_count += 1
        if error_count == num:
            print('На сегодня хватит.')
            break
        continue
