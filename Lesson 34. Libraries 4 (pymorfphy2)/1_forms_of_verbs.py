import pymorphy2
import sys


mrph = pymorphy2.MorphAnalyzer()
words = ['видеть', 'увидеть', 'глядеть', 'примечать', 'узреть']
text = ' '.join(map(str.rstrip, sys.stdin))
text = ''.join(list(filter(lambda x: x.isalpha() or x == ' ', text))).split(' ')
count = 0
for el in text:
    if mrph.parse(el)[0].normal_form in words:
        count += 1
print(count)
