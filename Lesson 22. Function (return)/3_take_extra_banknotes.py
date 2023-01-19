def take_large_banknotes(banknotes: list[int]) -> list[int]:
    large_banknotes = []
    for banknote in banknotes:
        if banknote > 10:
            large_banknotes.append(banknote)
    return large_banknotes


# print(*take_large_banknotes([]))
# print(*take_large_banknotes([1, 5, 500, 0.5, 2, 0.1, 10, 100, 100, 1000, 50]))
