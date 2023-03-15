string = input()
for i in range(len(string) // 2 + len(string) % 2):
    print(string[i:len(string) - i])