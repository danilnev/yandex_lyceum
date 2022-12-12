num1 = int(input())
dictionary = dict()
for i in range(num1):
    string = input()
    key = string.split()[0]
    value = ' '.join(string.split()[1:])
    dictionary[key] = value
num2 = int(input())
for i in range(num2):
    key = input()
    print(dictionary.get(key, 'Нет в словаре'))
