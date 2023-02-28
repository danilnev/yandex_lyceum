def recursive_len(some_list):
    if not some_list:
        return 0
    if some_list == [some_list[0]]:
        return 1
    else:
        return recursive_len(some_list[:-1]) + 1
