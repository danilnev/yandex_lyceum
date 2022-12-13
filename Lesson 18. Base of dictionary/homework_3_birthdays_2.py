num1 = int(input())
birthdays = dict()
for i in range(num1):
    name, day, month = [word for word in input().split()]
    if month not in birthdays:
        birthdays[month] = dict()
    if day not in birthdays[month]:
        birthdays[month][day] = []
    birthdays[month][day].append(name)
num2 = int(input())
for i in range(num2):
    month = input()
    if month not in birthdays:
        print()
    else:
        days = [int(key) for key in birthdays[month].keys()]
        days.sort()
        array = []
        for day in days:
            birthdays[month][str(day)].sort()
            for name in birthdays[month][str(day)]:
                array.append(f'{name} {str(day)}')
        print(' '.join(array))
