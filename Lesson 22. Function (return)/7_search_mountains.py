def find_mountain(heightsMap: list[list]) -> tuple:
    max_height = max([max(row) for row in heightsMap])
    for i in range(len(heightsMap)):
        for j in range(len(heightsMap[i])):
            if heightsMap[i][j] == max_height:
                return i, j


# a = [[1, 3, 1], [3, 2, 5], [2, 2, 2]]
# print(find_mountain(a))
# a = [[2, 4, 2, 3, 2], [3, 2, 3, 4, 3]]
# row, col = find_mountain(a)
# print(a[row][col])
