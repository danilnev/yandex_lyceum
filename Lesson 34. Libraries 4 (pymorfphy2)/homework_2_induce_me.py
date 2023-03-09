import pymorphy2
import itertools


word = input()
suits = {
    'Именительный падеж': 'nomn',
    'Родительный падеж': 'gent',
    'Дательный падеж': 'datv',
    'Винительный падеж': 'accs',
    'Творительный падеж': 'ablt',
    'Предложный падеж': 'loct'
}
mrph = pymorphy2.MorphAnalyzer()
parse = mrph.parse(word)[0]
if 'NOUN' not in parse.tag:
    print('Не существительное')
else:
    print('Единственное число:')
    for suit in suits:
        print(f'{suit}: {parse.inflect({"sing", suits[suit]}).word}')
    print('Множественное  число:')
    for suit in suits:
        print(f'{suit}: {parse.inflect({"plur", suits[suit]}).word}')
