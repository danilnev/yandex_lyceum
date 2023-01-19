def print_document(pages: list[str]) -> str:
    secret = False
    not_secret_pages = []
    for page in pages:
        if page.startswith('Секретно'):
            secret = True
            break
        else:
            not_secret_pages.append(page)
    if secret:
        not_secret_pages.append('Дальнейшие материалы засекречены')
    else:
        not_secret_pages.append('Напечатано без купюр')
    print('\n'.join(not_secret_pages))


# print_document(["Обычная страница", "И еще страница", "Секретно Вот этот вот текст не показывать", "Никому",
#                 "Никогда"])
# # print_document(["Пустой трёп", "который", "никому не интересен"])
