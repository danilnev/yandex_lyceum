def make_shades(alley: list[int], k: int) -> list[bool]:
    alley_places = [False for i in range(len(alley))]
    if k > 0:
        for i in range(len(alley)):
            if alley[i] != 0:
                metres = k * alley[i] + 1
                for j in range(0, metres):
                    if j + i >= len(alley):
                        break
                    alley_places[j + i] = True
    elif k == 0:
        for i in range(len(alley)):
            if alley[i] > 0:
                alley_places[i] = True
    elif k < 0:
        for i in range(len(alley)):
            if alley[i] != 0:
                metres = abs(k) * alley[i] + 1
                for j in range(0, metres):
                    if (i - j) >= 0:
                        alley_places[i - j] = True
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
