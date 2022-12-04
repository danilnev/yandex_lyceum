num_strings = int(input())
line = []
for i in range(num_strings):
    string = input()
    if string.startswith('Кто последний?'):
        line.append(string[19:-1])
    elif string == 'Следующий!':
        if line:
            print(f'Заходит {line[0]}!')
            line.pop(0)
        else:
            print('В очереди никого нет.')
    else:
        line.insert(0, string[23:-1])
