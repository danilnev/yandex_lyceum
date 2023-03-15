last = ''
goods = 0
bads = 0
while True:
    string = input()
    if string == 'добрый':
        goods += 1
        last = string
    elif string == 'злой':
        bads += 1
        last = string
    elif string == 'Какой подарок?':
        if goods > bads and last == 'добрый':
            print('серебряный шиллинг')
        elif bads > goods and last == 'злой':
            print('золотой')
        else:
            print('Ах, не знаю!')
            break
        goods = 0
        bads = 0
    else:
        break