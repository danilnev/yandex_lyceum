import random


def attempt(number, attempt_nums):  # возвращает кол-во быков и коров
    bulls = 0
    for i, j in zip(number.copy(), attempt_nums.copy()):  # по порядку сверяем цифры для нахождение кол-ва быков
        if i == j:
            bulls += 1
            number.remove(i)
            attempt_nums.remove(j)
    cows = len(set(number).intersection(set(attempt_nums)))  # ищем пары из оставшихся цифр для нахождения кол-ва коров
    return bulls, cows


main_number = random.randint(1000, 10000)  # случайно генерируем номер
attempt_num = int(input())
while main_number != attempt_num:  # цикл до момента, когда загаданное число и число пользователя будут равны
    bulls, cows = attempt(list(map(int, str(main_number))), list(map(int, str(attempt_num))))  # запрашиваем кол-ва
    new_main_number = random.randint(1000, 10000)  # заново генерируем номер, пока коровы и быки этого номера
    # не будут равны коровам и быкам старого номера
    while attempt(list(map(int, str(main_number))), list(map(int, str(new_main_number)))) != (bulls, cows):
        new_main_number = random.randint(1000, 10000)
    print(f'Bulls: {bulls}', f'Cows: {cows}', sep='\n')
    main_number = new_main_number
    attempt_num = int(input())
print('Поздравляю, вы выиграли!')
