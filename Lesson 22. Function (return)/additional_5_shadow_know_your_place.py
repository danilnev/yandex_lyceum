def make_shades(alley: list[int], k: int) -> list[bool]:
    alley_places = [False for i in range(len(alley))]
    if k > 0:
        for i in range(len(alley)):
            pass
    return alley_places


def calculate_sunny_length(shades: list[bool]) -> int:
    index = 0
    for shade in shades:
        if not shade:
            index += 1
    return index


def main():
    k = int(input())
    shadows = [int(x) for x in input().split()]
    shadows_and_sunny = make_shades(shadows, k)
    metres = calculate_sunny_length(shadows_and_sunny)
    if metres >= 10:
        print('Обгорел')
    else:
        print('Тени достаточно')


# print(make_shades([0, 0, 0, 4, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 3, 0], 1))
# print(calculate_sunny_length([True, True, True, True, True, True, False, False, False, True, True, True, True, True,
#                               True, True, False]))
# main()
