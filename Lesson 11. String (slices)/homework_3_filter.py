num = int(input())
for i in range(num):
    string = input()
    if string[:4] == '####':
        continue
    elif string[:2] == '%%':
        print(string[2:])
    else:
        print(string)