classic_print = print


def print(*args, **kwargs):
    upper_args = list(map(lambda x: str(x).upper(), args))
    classic_print(*upper_args)
