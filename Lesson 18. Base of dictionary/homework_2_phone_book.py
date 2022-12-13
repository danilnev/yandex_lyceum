num1 = int(input())
phone_book = dict()
for i in range(num1):
    number, name = input().split()
    if name not in phone_book:
        phone_book[name] = [number]
    else:
        phone_book[name].append(number)
num2 = int(input())
for i in range(num2):
    name = input()
    if name in phone_book:
        print(' '.join(phone_book[name]))
    else:
        print('Нет в телефонной книге')
