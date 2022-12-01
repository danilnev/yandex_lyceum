symbols = input().split()
numbers = []
for symbol in symbols:
    if symbol.isdigit():
        numbers.append(int(symbol))
    else:
        if symbol == '+':
            summ = numbers[-1] + numbers[-2]
            numbers = numbers[:-2]
            numbers.append(summ)
        elif symbol == '-':
            diff = numbers[-2] - numbers[-1]
            numbers = numbers[:-2]
            numbers.append(diff)
        elif symbol == '*':
            mltp = numbers[-1] * numbers[-2]
            numbers = numbers[:-2]
            numbers.append(mltp)
print(numbers[0])
