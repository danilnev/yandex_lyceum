symbols = list(input())
numbers = [0 for i in range(30000)]
car_x = 0
i = 0
while i < len(symbols):
    symbol = symbols[i]
    if symbol == '>':
        if car_x == 29999:
            car_x = 0
        else:
            car_x += 1
    elif symbol == '<':
        if car_x == 0:
            car_x = 29999
        else:
            car_x -= 1
    elif symbol == '+':
        numbers[car_x] += 1
        numbers[car_x] %= 256
    elif symbol == '-':
        if numbers[car_x] == 0:
            numbers[car_x] = 255
        else:
            numbers[car_x] -= 1
    elif symbol == '.':
        print(numbers[car_x])
    elif symbol == '[':
        if numbers[car_x] == 0:
            while symbol != ']':
                i += 1
                symbol = symbols[i]
    elif symbol == ']':
        if numbers[car_x] != 0:
            while symbol != '[':
                i -= 1
                symbol = symbols[i]
    i += 1
