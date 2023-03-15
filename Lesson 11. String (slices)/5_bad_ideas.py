n = int(input())
for i in range(n):
    string = input()
    if string[:3] == 'не ' or string[:3] == 'Не ':
        print(string[3:])
    else:
        print(string)