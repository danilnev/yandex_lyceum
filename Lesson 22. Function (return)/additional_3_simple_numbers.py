def prime(number: int) -> str:
    simple_numbers = [2]
    for i in range(3, int(number ** 0.5) + 1, 2):
        flag = True
        for num in simple_numbers:
            if i % num == 0:
                flag = False
                break
            if num > i:
                break
        if flag:
            simple_numbers.append(i)
    flag = True
    for simple_number in simple_numbers:
        if number % simple_number == 0:
            flag = False
            break
    if flag:
        return 'Простое число'
    else:
        return 'Составное число'


# print(prime(4))
# print(prime(3))
# print(prime(59))
# print(prime(173))
# print(prime(195))
