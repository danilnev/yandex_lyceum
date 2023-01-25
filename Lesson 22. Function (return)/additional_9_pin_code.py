def issimple(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            return False
    return True


def ispalindrome(num):
    reverse_num = int(''.join(reversed(list(str(num)))))
    if num == reverse_num:
        return True
    else:
        return False


def is_degree_of_two(num):
    i = 0
    while 2 ** i <= num:
        if 2 ** i == num:
            return True
        i += 1
    return False


def check_pin(pinCode):
    a, b, c = [int(num) for num in pinCode.split('-')]
    if issimple(a) and ispalindrome(b) and is_degree_of_two(c):
        return 'Корректен'
    else:
        return 'Некорректен'


# print(check_pin('7-101-4'))
# print(check_pin('12-22-16'))
# print(check_pin('1-101-32'))
