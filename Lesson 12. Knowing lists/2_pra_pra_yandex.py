listt = list()
num = int(input())
for i in range(num):
    listt.append(input())
search_word = input()
for string in listt:
    if search_word in string:
        print(string)