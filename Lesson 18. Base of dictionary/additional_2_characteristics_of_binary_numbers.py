numbers = [int(number) for number in input().split()]
dicts = []
for number in numbers:
    num = number
    division = ''
    two_number = []
    while num != 0:
        two_number.insert(0, str(num % 2))
        num //= 2
    two_number = ''.join(two_number)
    digits = len(two_number)
    units = two_number.count('1')
    zeros = two_number.count('0')
    dicts.append({'digits' : digits, 'units' : units, 'zeros' : zeros})
print(dicts)
