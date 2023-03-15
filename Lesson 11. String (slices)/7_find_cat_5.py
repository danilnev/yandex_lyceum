num = int(input())
for i in range(num):
    string = input()
    for j in range(len(string)):
        if string[j:j + 3] == 'кот':
            print(i + 1, j + 1)
            break
