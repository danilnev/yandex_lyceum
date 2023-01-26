def transpose(matrix):
    transposition_field = [[' ' for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposition_field[j][i] = matrix[i][j]
    matrix.clear()
    matrix.extend(transposition_field)


# matrix = [[1, 2, 3], [4, 5, 6]]
# transpose(matrix)
# for line in matrix:
#     print(*line)
