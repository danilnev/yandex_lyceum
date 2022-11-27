num = int(input())
numbers = []
for i in range(num):
    numbers.append(int(input()))
for i in range(num):
    for j in range(num):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
for number in numbers:
    print(number)