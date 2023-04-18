def cached(func):
    cache = dict()

    def wrapper(*args, **kwargs):
        if args[0] in cache:
            return cache[args[0]]
        result = func(*args, **kwargs)
        cache[args[0]] = result
        return result
    return wrapper
