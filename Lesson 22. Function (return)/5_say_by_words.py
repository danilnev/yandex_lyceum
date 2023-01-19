def number_in_english(number: int) -> str:
    numbers = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
               6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
               11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
               16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
               20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
               60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred'
               }
    if (number <= 20 or number % 10 == 0 or number == 0) and number < 100:
        return numbers[number]
    elif number % 100 == 0:
        return numbers[int(str(number)[0])] + ' ' + numbers[100]
    elif number <= 99:
        return numbers[int(str(number)[0] + '0')] + ' ' + numbers[int(str(number)[1])]
    elif int(str(number)[1:]) > 20:
        return numbers[int(str(number)[0])] + ' ' + numbers[100] + ' and ' + numbers[int(str(number)[1] + '0')] + ' ' \
            + numbers[int(str(number)[2])]
    else:
        return numbers[int(str(number)[0])] + ' ' + numbers[100] + ' and ' + numbers[int(str(number)[1:])]


# print(number_in_english(0))
# print(number_in_english(1))
# print(number_in_english(78))
# print(number_in_english(115))
# print(number_in_english(729))
# print(number_in_english(100).lower())
