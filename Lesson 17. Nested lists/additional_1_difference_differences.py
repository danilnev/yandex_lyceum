num = int(input())
numbers = [int(input()) for i in range(num)]
differences = []
for number in numbers:
    for number_diff in numbers:
        difference = number - number_diff
        if difference not in differences:
            differences.append(difference)
differences.sort()
print('\n'.join([str(number) for number in differences]))
