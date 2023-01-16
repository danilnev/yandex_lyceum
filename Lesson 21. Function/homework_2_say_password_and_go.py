def ask_password():
    flag = True
    for i in range(3):
        password = input()
        if password == 'password':
            print('Пароль принят')
            flag = False
            break
    if flag:
        print('В доступе отказано')


# ask_password()
