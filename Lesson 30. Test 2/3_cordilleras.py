import functools


def mountains(*args, **kwargs):
    if 'second_longer' in kwargs:
        args = list(filter(lambda x: len(x[1]) - len(x[0]) >= kwargs['second_longer'], args))
    if 'first_smaller' in kwargs:
        if kwargs['first_smaller']:
            args = list(filter(lambda x: x[0][0].lower() < x[1][-1].lower(), args))
        else:
            args = list(filter(lambda x: x[0][0].lower() >= x[1][-1].lower(), args))
    if 'common_letters' in kwargs:
        array = list(map(set, args))
        array = list(functools.reduce(lambda a, b: a.intersection(b), array))
        if len(array) > kwargs['common_letters']:
            return
    if 'presence' in kwargs:
        args = list(filter(lambda x: kwargs['presence'] in x[1], args))
    return max(map(lambda x: x[0], args)), sum(map(lambda x: len(x[1]), args))
