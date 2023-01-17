def print_long_words(text):
    rus = ['а', 'о', 'э', 'и', 'у', 'ы', 'е', 'ё', 'ю', 'я']
    eng = ['a', 'e', 'i', 'o', 'u', 'y']
    i = 0
    while i < len(text):
        word = ''
        letter = text[i]
        while letter.isalpha():
            word += letter
            i += 1
            if i < len(text):
                letter = text[i]
            else:
                break
        i += 1
        if word.isalnum():
            word = word.lower()
            count_rus = 0
            count_eng = 0
            for letter in rus:
                count_rus += word.count(letter)
            for letter in eng:
                count_eng += word.count(letter)
            if count_rus >= 4 or count_eng >= 4:
                print(word)


# print_long_words('Как и в прочих заданиях этого урока, в вашем решении функция должна быть определена, '
#                  'но не должна вызываться.')
# print_long_words('The five boxing wizards jump quickly')
