num1 = int(input())
birthdays = dict()
for i in range(num1):
    name, day, month = [word for word in input().split()]
    if month not in birthdays:
        birthdays[month] = []
    birthdays[month].append(name)
num2 = int(input())
for i in range(num2):
    month = input()
    if month not in birthdays:
        print()
    else:
        birthdays[month].sort()
        print(' '.join(birthdays[month]))
