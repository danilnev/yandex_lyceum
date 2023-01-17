def eratosthenes(N):
    numbers = [i for i in range(2, N + 1)]
    deleted = []
    i = 2
    while True:
        flag1 = True
        flag2 = True
        for number in numbers:
            if number % i == 0 and number != i:
                deleted.append(str(number))
                numbers.remove(number)
                flag2 = False
        for number in numbers:
            if number > i:
                i = number
                flag = False
                break
        if flag1 and flag2:
            break
    print(' '.join(deleted))


# eratosthenes(15)
