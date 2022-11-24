num = int(input())
numbers = [1, 1, 1]
if num <= 3:
    for i in range(num):
        print(numbers[i], end=' ')
else:
    for i in range(num - 3):
        numbers.append(numbers[i] + numbers[i + 1] + numbers[i + 2])
    for number in numbers:
        print(number, end=' ')