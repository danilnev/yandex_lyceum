import random


def attempt(number, attempt_nums):
    bulls = 0
    for i, j in zip(number.copy(), attempt_nums.copy()):
        if i == j:
            bulls += 1
            number.remove(i)
            attempt_nums.remove(j)
    cows = len(set(number).intersection(set(attempt_nums)))
    return bulls, cows


main_number = random.randint(1000, 10000)
attempt_num = int(input())
while main_number != attempt_num:
    bulls, cows = attempt(list(map(int, str(main_number))), list(map(int, str(attempt_num))))
    new_main_number = random.randint(1000, 10000)
    while attempt(list(map(int, str(main_number))), list(map(int, str(new_main_number)))) != (bulls, cows):
        new_main_number = random.randint(1000, 10000)
    print(f'Bulls: {bulls}', f'Cows: {cows}', sep='\n')
    main_number = new_main_number
    attempt_num = int(input())
print('Поздравляю, вы выиграли!')
