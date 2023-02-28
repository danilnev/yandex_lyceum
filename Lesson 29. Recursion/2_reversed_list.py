def recursive_reverse(some_list):
    if len(some_list) == 0:
        return []
    elif len(some_list) == 1:
        return some_list
    elif len(some_list) == 2:
        return some_list[::-1]
    else:
        return [some_list[-1]] + recursive_reverse(some_list[1:-1]) + [some_list[0]]
