words = list()
num = int(input())
for i in range(num):
    words.append(input())
letter_index = int(input())
for word in words:
    if len(word) >= letter_index:
        print(word[letter_index - 1], end='')