def pass_check(password):
    return password == 'g'


def check_password(old_func):
    def wrapper(*args, **kwargs):
        password = input()
        if pass_check(password):
            return old_func(*args, **kwargs)
        else:
            print('В доступе отказано')
            return None
    return wrapper


@check_password
def fib(n):
    return fibbonaci(n)


def fibbonaci(n):
    if n <= 2:
        return 1
    return fibbonaci(n - 1) + fibbonaci(n - 2)
