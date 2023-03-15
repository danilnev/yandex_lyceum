while True:
    num1 = int(input())
    value = input()
    if value == '!':
        if num1 < 0:
            continue
        else:
            result = 1
            for i in range(2, num1 + 1):
                result *= i
    elif value == 'x':
        print(num1)
        break
    else:
        num2 = int(input())
        if value == '+':
            result = num1 + num2
        elif value == '-':
            result = num1 - num2
        elif value == '*':
            result = num1 * num2
        elif value == '%':
            if num2 != 0:
                result = num1 % num2
            else:
                continue
        else:
            if num2 != 0:
                result = num1 // num2
            else:
                continue
    print(result)
