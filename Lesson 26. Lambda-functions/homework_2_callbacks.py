def ask_password(login, password, success, failure):
    vovels = ['a', 'e', 'i', 'o', 'u', 'y']
    vov_count = 0
    login = login.lower()
    password = password.lower()
    pass_without_vov = ''
    login_without_vov = ''
    for letter in password:
        if letter in vovels:
            vov_count += 1
        else:
            pass_without_vov += letter
    for letter in login:
        if letter not in vovels:
            login_without_vov += letter
    if vov_count != 3 and login_without_vov != pass_without_vov:
        failure(login, 'Everything is wrong')
    elif vov_count != 3:
        failure(login, 'Wrong number of vowels')
    elif login_without_vov != pass_without_vov:
        failure(login, 'Wrong consonants')
    else:
        success(login)


def succes(login):
    print(f'Привет, {login}!')


def failure(login, error_str):
    print(f'Кто-то пытался притвориться пользователем {login}, но в пароле допустил ошибку: {error_str.upper()}.')


def main(login, password):
    ask_password(login, password, succes, failure)
