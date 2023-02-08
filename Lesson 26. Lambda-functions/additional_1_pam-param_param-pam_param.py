phrases = input().split()
vovels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
lengths = []
for phrase in phrases:
    lengths.append(len(list(filter(lambda x: x in vovels, list(phrase)))))
if min(lengths) == max(lengths):
    print('Парам пам-пам')
else:
    print('Пам парам')
