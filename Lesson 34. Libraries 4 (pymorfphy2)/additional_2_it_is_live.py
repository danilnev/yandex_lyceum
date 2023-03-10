import sys
import pymorphy2


mrph = pymorphy2.MorphAnalyzer()
words = list(map(str.rstrip, sys.stdin))
for word in words:
    if 'NOUN' not in mrph.parse(word)[0].tag:
        print('Не существительное')
    else:
        analys = mrph.parse(word)[0]
        if 'anim' in analys.tag:
            if 'sing' in analys.tag:
                if 'masc' in analys.tag:
                    print('Живой')
                elif 'femn' in analys.tag:
                    print('Живая')
                else:
                    print('Живое')
            else:
                print('Живые')
        else:
            if 'sing' in analys.tag:
                if 'masc' in analys.tag:
                    print('Не живой')
                elif 'femn' in analys.tag:
                    print('Не живая')
                else:
                    print('Не живое')
            else:
                print('Не живые')
