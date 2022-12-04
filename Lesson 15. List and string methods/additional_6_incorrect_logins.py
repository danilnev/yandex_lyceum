logins = input().split(',')
right_english = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
right_symbols = '0123456789_'
right_russian = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
incorrect_logins = []
for login in logins:
    for symbol in login:
        if symbol not in right_russian and symbol not in right_english and symbol not in right_symbols:
            incorrect_logins.append(login)
            break
if incorrect_logins:
    lengths = [len(login) for login in incorrect_logins]
    string_len = max(lengths)
    incorrect_logins.sort()
    for login in incorrect_logins:
        print(login.rjust(string_len, ' '))
