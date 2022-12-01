peoples = []
string = input()
while string != '':
    people = string.split(':')
    name = people[4].split(', ')[0]
    peoples.append((people[0], people[1], name))
    string = input()
passwords = input().split(';')
for people in peoples:
    for password in passwords:
        if people[1] == password:
            print('To: ', people[0], '\n', people[2], ', ваш пароль слишком простой, смените его.', sep='')
            break
