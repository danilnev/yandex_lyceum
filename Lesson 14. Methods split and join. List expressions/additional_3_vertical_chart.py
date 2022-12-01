numbers = input().split()
maxx = 0
for number in numbers:
    if int(number) > maxx:
        maxx = int(number)
print('*' * (len(numbers) + 2), '\n', '*', (' ' * len(numbers)), '*', sep='')
for i in range(maxx, 0, -1):
    print('*', end='')
    for number in numbers:
        if i > int(number):
            print(' ', end='')
        else:
            print('*', end='')
    print('*')
