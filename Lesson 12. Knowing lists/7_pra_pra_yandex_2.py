num1 = int(input())
strings = list()
search_words = list()
for i in range(num1):
    strings.append(input())
num2 = int(input())
for i in range(num2):
    search_words.append(input())
for string in strings:
    flag = True
    for word in search_words:
        if word not in string:
            flag = False
            break
    if flag:
        print(string)