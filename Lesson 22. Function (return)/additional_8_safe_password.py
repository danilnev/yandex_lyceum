def password_level(password: str):
    if len(password) < 6:
        return 'Недопустимый пароль'
    elif password.isdigit() or \
            (((password.lower() == password) or (password.upper() == password)) and password.isalpha()):
        return 'Ненадежный пароль'
    elif password.isalpha() or \
            ((password.lower() == password) or (password.upper() == password) and not password.isdigit()):
        return 'Слабый пароль'
    else:
        return 'Надежный пароль'


# print(password_level("qwerty12345"))
# print(password_level("12345фывапр"))
# print(password_level("12345ASDS"))
# print(password_level("qwerty"))
# print(password_level("123Qwerty"))
# print(password_level("Qwerty"))
