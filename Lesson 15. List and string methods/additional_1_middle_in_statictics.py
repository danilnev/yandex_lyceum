numbers = [float(number) for number in input().split()]
num1 = float()
for number in numbers:
    num1 += number
num1 /= len(numbers)
numbers.sort()
if len(numbers) % 2 == 1:
    num2 = numbers[len(numbers) // 2]
else:
    num2 = (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
print(num1, num2)
