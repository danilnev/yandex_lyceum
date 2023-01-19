def average(values: list[int]) -> float:
    if len(values) == 0:
        return 0
    else:
        return sum(values) / len(values)


# print(average([1, 5, 500, 10]))
# print(average([1, 2, 3, 4, 5]))
# print(average([-5, 2]))
