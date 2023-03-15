num = int(input())
for i in range(num):
    for j in range(i, -1, -1):
        print('Осталось секунд:', j)
    print('Пуск', i + 1)