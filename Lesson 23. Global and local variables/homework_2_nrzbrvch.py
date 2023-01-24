def translate(text: str):
    global translated_text, vowels
    words = []
    for word in text.split():
        string = ''
        for letter in word:
            if letter.isalpha() and letter.lower() not in vowels:
                string += letter
        if string:
            words.append(string)
    translated_text = ' '.join(words)


vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
# translated_text = None
# translate("Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно просто читать. Достаточно небольшой "
#           "тренировки - и вы сможете это делать.")
# print(translated_text)
