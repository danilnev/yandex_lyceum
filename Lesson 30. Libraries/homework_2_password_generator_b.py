import random
import string


def generate_password(m):
    global abc
    password = ''.join(random.sample(abc, k=m))
    while len(list(filter(lambda x: x.isdigit(), password))) < 1 or \
            len(list(filter(lambda x: x in string.ascii_lowercase, password))) < 1 or \
            len(list(filter(lambda x: x in string.ascii_uppercase, password))) < 1:
        password = ''.join(random.sample(abc, k=m))
    return password


def main(n, m):
    ps = []
    for i in range(n):
        password = generate_password(m)
        while password in ps:
            password = generate_password(m)
        ps.append(password)
    return ps


abc = 'abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'
print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")
