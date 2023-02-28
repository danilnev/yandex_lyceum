def rec_linear_sum(some_list):
    if len(some_list) == 0:
        return 0
    else:
        return some_list[0] + rec_linear_sum(some_list[1:])
