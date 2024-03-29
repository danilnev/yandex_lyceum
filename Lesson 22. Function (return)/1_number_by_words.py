def number_to_words(n: int) -> str:
    numbers = {
        0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
        6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять',
        11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать',
        16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать', 20: 'двадцать',
        30: 'тридцать', 40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят',
        80: 'восемьдесят', 90: 'девяносто'
    }

    if n <= 20 or n % 10 == 0:
        return numbers[n]
    else:
        return numbers[int(str(n)[0] + '0')] + ' ' + numbers[int(str(n)[1])]


# print(number_to_words(4))
# print(number_to_words(13))
# print(number_to_words(57))
# print(number_to_words(30))
