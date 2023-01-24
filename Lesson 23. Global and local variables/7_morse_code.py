def encode_to_morse(text: str, lan: str):
    global ru_to_morse_code, en_to_morse_code
    code = []
    not_in_code_symbols = []
    if lan == 'ru':
        for letter in text.lower():
            if letter in ru_to_morse_code:
                code.append(ru_to_morse_code[letter])
            else:
                not_in_code_symbols.append(letter)
    elif lan == 'en':
        for letter in text.lower():
            if letter in en_to_morse_code:
                code.append(en_to_morse_code[letter])
            else:
                not_in_code_symbols.append(letter)
    else:
        return '', ''
    if not not_in_code_symbols:
        return ' '.join(code), 0
    else:
        return ' '.join(code), f'Нераспознанные символы: {", ".join(not_in_code_symbols)}'


def decode_from_morse(code: str, lan: str):
    global morse_code_to_ru, morse_code_to_end
    string = ''
    not_in_code_symbols = []
    if lan == 'ru':
        for symbol in code.split():
            if symbol in morse_code_to_ru:
                string += morse_code_to_ru[symbol]
            else:
                not_in_code_symbols.append(symbol)
    elif lan == 'en':
        for symbol in code.split():
            if symbol in morse_code_to_en:
                string += morse_code_to_en[symbol]
            else:
                not_in_code_symbols.append(symbol)
    else:
        return '', ''
    if not not_in_code_symbols:
        return string, 0
    else:
        return string, f'Нераспознанные символы: {", ".join(not_in_code_symbols)}'


def main():
    global help_commands
    print('Привет, я программа кодировки и декодировки слов, используя Азбуку Морзе!')
    print(help_commands)
    while True:
        command = input()
        if command == 'encode':
            lang = input('Введите язык (ru, en): ')
            text = input('Введите текст на русском языке: ')
            code, error = encode_to_morse(text, lang)
            if code == '':
                print('Ошибка: не удалось распознать текст.')
            else:
                print(code)
                if error == 0:
                    print('Нераспознанных символов нет.')
                else:
                    print(error)
        elif command == 'decode':
            morse_code = input('Введите код на Азбуке Морзе: ')
            lang = input('Введите язык перевода (ru, en): ')
            text, error = decode_from_morse(morse_code, lang)
            if text == '':
                print('Ошибка: не удалось распознать текст.')
            else:
                print(text)
                if error == 0:
                    print('Нераспознанных символов нет.')
                else:
                    print(error)
        elif command == 'help':
            print(help_commands)
        elif command == 'exit':
            break
        else:
            print('Ошибка: нераспознанная комманда.')
            continue
    print('Программа завершила свою работу, удачи!')


en_to_morse_code = {'a': '.-', 'b': '-...',
                    'c': '-.-.', 'd': '-..', 'e': '.',
                    'f': '..-.', 'g': '--.', 'h': '....',
                    'i': '..', 'j': '.---', 'k': '-.-',
                    'l': '.-..', 'm': '--', 'n': '-.',
                    'o': '---', 'p': '.--.', 'q': '--.-',
                    'r': '.-.', 's': '...', 't': '-',
                    'u': '..-', 'v': '...-', 'w': '.--',
                    'x': '-..-', 'y': '-.--', 'z': '--..',
                    '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ',': '--..--', '.': '.-.-.-',
                    '?': '..--..', '/': '-..-.', '-': '-....-',
                    '(': '-.--.', ')': '-.--.-', '!': '-.-.--',
                    ' ': '-...-'}
morse_code_to_en = {'.-': 'a', '-...': 'b',
                    '-.-.': 'c', '-..': 'd', '.': 'e',
                    '..-.': 'f', '--.': 'g', '....': 'h',
                    '..': 'i', '.---': 'j', '-.-': 'k',
                    '.-..': 'l', '--': 'm', '-.': 'n',
                    '---': 'o', '.--.': 'p', '--.-': 'q',
                    '.-.': 'r', '...': 's', '-': 't',
                    '..-': 'u', '...-': 'v', '.--': 'w',
                    '-..-': 'x', '-.--': 'y', '--..': 'z',
                    '.----': '1', '..---': '2', '...--': '3',
                    '....-': '4', '.....': '5', '-....': '6',
                    '--...': '7', '---..': '8', '----.': '9',
                    '-----': '0', '--..--': ',', '.-.-.-': '.',
                    '..--..': '?', '-..-.': '/', '-....-': '-',
                    '-.--.': '(', '-.--.-': ')', '-.-.--': '!',
                    '-...-': ' '}
ru_to_morse_code = {'а': '.-', 'б': '-...', 'в': '.--',
                    'г': '--.', 'д': '-..', 'е': '.',
                    'ж': '...-', 'з': '--..', 'и': '..',
                    'й': '.---', 'к': '-.-', 'л': '.-..',
                    'м': '--', 'н': '-.', 'о': '---',
                    'п': '.--.', 'р': '.-.', 'с': '...',
                    'т': '-', 'у': '..-', 'ф': '..-.',
                    'х': '....', 'ц': '-.-.', 'ч': '---.',
                    'ш': '----', 'щ': '--.-', 'ъ': '.--.-.',
                    'ы': '-.--', 'ь': '-..-', 'э': '..-..',
                    'ю': '..--', 'я': '.-.-', '1': '.----',
                    '2': '..---', '3': '...--',
                    '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ',': '--..--', '.': '.-.-.-',
                    '?': '..--..', '/': '-..-.', '-': '-....-',
                    '(': '-.--.', ')': '-.--.-', '!': '-.-.--',
                    ' ': '-...-'}
morse_code_to_ru = {'.-': 'а', '-...': 'б', '.--': 'в',
                    '--.': 'г', '-..': 'д', '.': 'е',
                    '...-': 'ж', '--..': 'з', '..': 'и',
                    '.---': 'й', '-.-': 'к', '.-..': 'л',
                    '--': 'м', '-.': 'н', '---': 'о',
                    '.--.': 'п', '.-.': 'р', '...': 'с',
                    '-': 'т', '..-': 'у', '..-.': 'ф',
                    '....': 'х', '-.-.': 'ц', '---.': 'ч',
                    '----': 'ш', '--.-': 'щ', '.--.-.': 'ъ',
                    '-.--': 'ы', '-..-': 'ь', '..-..': 'э',
                    '..--': 'ю', '.-.-': 'я',
                    '.----': '1', '..---': '2', '...--': '3',
                    '....-': '4', '.....': '5', '-....': '6',
                    '--...': '7', '---..': '8', '----.': '9',
                    '-----': '0', '--..--': ',', '.-.-.-': '.',
                    '..--..': '?', '-..-.': '/', '-....-': '-',
                    '-.--.': '(', '-.--.-': ')', '-.-.--': '!',
                    '-...-': ' '
                    }
help_commands = 'Список комманд: encode (закодировать), decode (разкодировать), help (список комманд), exit (выйти)'
main()
