num = int(input())
numbers = [0]
print(0)
for i in range(num - 1):
    count = 0
    for j in range(len(numbers)):
        if numbers[j] == numbers[len(numbers) - j - 1]:
            count += 1
    numbers.append(count)
    print(count)