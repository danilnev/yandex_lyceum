def check_password(ps):
    def generator(old_func):
        def wrapper(*args, **kwargs):
            password = input()
            if password == ps:
                return old_func(*args, **kwargs)
            else:
                print('В доступе отказано')
                return None

        return wrapper
    return generator
