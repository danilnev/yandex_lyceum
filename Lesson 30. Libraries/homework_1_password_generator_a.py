import random


def generate_password(m):
    global abc
    return ''.join(random.sample(abc, k=m))


def main(n, m):
    ps = []
    for i in range(n):
        password = generate_password(m)
        while password in ps:
            password = generate_password(m)
        ps.append(password)
    return ps


abc = 'abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'