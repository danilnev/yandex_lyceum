import pymorphy2
import sys


morph = pymorphy2.MorphAnalyzer()
words_count = []
text = ' '.join(map(str.rstrip, sys.stdin))
text = ''.join(list(filter(lambda x: x.isalpha() or x == ' ' or x == '-', text)))
text = text.replace('-', ' ')
text = list(filter(lambda x: x, text.split()))
for word in text:
    if 'NOUN' in morph.parse(word)[0].tag and morph.parse(word)[0].score > 0.5:
        normal = morph.parse(word)[0].normal_form
        if normal not in map(lambda x: x[0], words_count):
            words_count.append([normal, 1])
        else:
            words_count[list(map(lambda x: x[0], words_count)).index(normal)][1] += 1
words_count.sort(key=lambda x: (x[1], x[0]), reverse=True)
print(*list(map(lambda x: x[0], words_count[:10])))
