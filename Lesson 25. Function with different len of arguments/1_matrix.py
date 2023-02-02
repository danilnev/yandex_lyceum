def matrix(*args):
    if len(args) == 0:
        return 0
    elif len(args) == 1:
        return [[0 for i in range(args[0])] for j in range(args[0])]
    elif len(args) == 2:
        return [[0 for i in range(args[0])] for j in range(args[1])]
    else:
        return [[args[2] for i in range(args[0])] for j in range(args[1])]


# print(matrix(5, 6, 10))
