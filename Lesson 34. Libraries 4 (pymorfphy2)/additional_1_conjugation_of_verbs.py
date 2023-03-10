import itertools
import pymorphy2


gender = ['masc', 'femn', 'neut']
nums = ['sing', 'plur']
masks = ['1per', '2per', '3per']
mrph = pymorphy2.MorphAnalyzer()
word = input()
analys = mrph.parse(word)[0]
if 'VERB' not in analys.tag and 'INFN' not in analys.tag:
    print('Не глагол')
else:
    print('Прошедшее время:')
    for el in gender:
        print(analys.inflect({'past', el}).word)
    print(analys.inflect({'past', 'plur'}).word)
    print('Настоящее время:')
    for mask, num in itertools.product(masks, nums):
        print(analys.inflect({mask, num}).word)

