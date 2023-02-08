def print_operation_table(operation, num_rows=9, num_columns=9):
    for i in range(1, num_rows + 1):
        row = list(map(operation, [i] * num_columns, range(1, num_columns + 1)))
        print('\t'.join(map(str, row)))


print_operation_table(lambda x, y: x * y)
