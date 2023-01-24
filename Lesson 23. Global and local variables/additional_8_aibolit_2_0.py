def hello(name):
    global query
    if None in query:
        window = query.index(None)
        print(f'Здравствуйте, {name}! Подойдите к окошку номер {window + 1}')
        query[window] = name
    else:
        print(f'Простите, {name}. Все окна заняты')


def search_card(name):
    global base, query
    if name in query:
        if name in base:
            print(f'Ваша карта с номером {base.index(name) + 1} найдена')
        else:
            print('Ваша карта не найдена')
    else:
        print(f'Простите, {name}, дождитесь своей очереди')


def good_bye(name):
    global query
    if name in query:
        print(f'До свидания, не болейте, {name}')
        query[query.index(name)] = None
    else:
        print(f'Простите, {name}, дождитесь своей очереди')


# base = ["Иван", "Юлия Иванкова"]
# query = [None, None, None]
#
# hello("Иван")
# search_card("Иван")
# hello("Юлия Иванова")
# search_card("Юлия Иванова")
