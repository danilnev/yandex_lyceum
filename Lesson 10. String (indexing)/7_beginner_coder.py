string = input()
for i in range(len(string)):
    if len(string) - i == 1:
        print(ord(string[i]))
    else:
        print(ord(string[i]), end=', ')