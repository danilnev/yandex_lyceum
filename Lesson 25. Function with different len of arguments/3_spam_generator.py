def make_letter(name, date, email, place='Рязань'):
    return '\n'.join([
        f'To: {email}',
        f'Здравствуйте, {name}!',
        f'Были бы рады видеть вас на встрече начинающих программистов в {place}, которая пройдет {date}.'
    ])


# print(make_letter('Яков', '02.02.2023', 'yakov@yandex.ru', 'IT-Куб'))
# print(make_letter('Николай', '03.02.2023', 'zhalnenko@yandex.ru'))
