import pymorphy2


morph = pymorphy2.MorphAnalyzer()
for i in range(99, 0, -1):
    if (i - 1) % 10 == 1 and i != 12:
        print(
            f'В холодильнике {i} {morph.parse("бутылка")[0].make_agree_with_number(i).word} кваса.',
            'Возьмём одну и выпьем.',
            f'Осталась {i - 1} {morph.parse("бутылка")[0].make_agree_with_number(i - 1).word} кваса.',
            sep='\n'
        )

    else:
        print(
            f'В холодильнике {i} {morph.parse("бутылка")[0].make_agree_with_number(i).word} кваса.',
            'Возьмём одну и выпьем.',
            f'Осталось {i - 1} {morph.parse("бутылка")[0].make_agree_with_number(i - 1).word} кваса.',
            sep='\n'
        )
