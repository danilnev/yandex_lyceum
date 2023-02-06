def arithmetic_operation(symb):
    if symb == '+':
        return lambda a, b: a + b
    elif symb == '-':
        return lambda a, b: a - b
    elif symb == '*':
        return lambda a, b: a * b
    else:
        return lambda a, b: a / b
