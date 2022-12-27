darks = {'Густая темнота': [], 'Плотная темнота': []}
num = int(input())
for i in range(num):
    number = int(input())
    if str(number) not in darks['Густая темнота'] and str(number) not in darks['Плотная темнота']:
        if number % 7 == 0:
            darks['Густая темнота'].append(str(number))
        elif (number + 1) % 7 == 0:
            darks['Плотная темнота'].append(str(number))
print(f'''Густая темнота ({'; '.join(darks['Густая темнота'])})''')
print(f'''Плотная темнота ({'; '.join(darks['Плотная темнота'])})''')
