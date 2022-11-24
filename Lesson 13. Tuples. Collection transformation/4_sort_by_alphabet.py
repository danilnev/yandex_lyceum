num = int(input())
words = []
for i in range(num):
    words.append(input())
for i in range(num):
    for j in range(num):
        if words[j] > words[i]:
            words[j], words[i] = words[i], words[j]
for word in words:
    print(word)