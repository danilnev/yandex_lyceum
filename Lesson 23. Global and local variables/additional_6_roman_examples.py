def num_to_roman(num: int):
    roman_num = ''
    while num > 0:
        for key in roman_system:
            while num >= key:
                roman_num += roman_system[key]
                num -= key
    return roman_num


def roman():
    global one, two, three
    three = one + two
    print(num_to_roman(one), '+', num_to_roman(two), '=', num_to_roman(three))


roman_system = {
    1000: 'M', 900: 'CM',
    500: 'D', 400: 'CD',
    100: 'C', 90: 'XC',
    50: 'L', 40: 'XL',
    10: 'X', 9: 'IX',
    5: 'V', 4: 'IV',
    1: 'I'
}
# one = 5
# two = 4
# roman()
