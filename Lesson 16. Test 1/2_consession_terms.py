numbers = [int(number) for number in input().split()]
middle = sum(numbers) / len(numbers)
result = set()
for number in numbers:
    if abs(number - middle) <= numbers[0]:
        result.add(str(number))
print(' '.join(result))
