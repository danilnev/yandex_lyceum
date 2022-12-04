numbers = [int(number) for number in input().split()]
numbers.sort()
if len(numbers) % 2 == 1:
    num1 = numbers[len(numbers) // 2]
else:
    num1 = (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
max_count = 0
for number in numbers:
    if numbers.count(number) > max_count:
        num2 = number
        max_count = numbers.count(number)
print(num1, num2)
