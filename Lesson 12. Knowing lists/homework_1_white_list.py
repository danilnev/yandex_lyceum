num1 = int(input())
white_list = list()
for i in range(num1):
    white_list.append(input())
num2 = int(input())
for i in range(num2):
    word = input()
    if word in white_list:
        print(word)