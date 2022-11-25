num = int(input())
words = []
for i in range(num):
    words.append(input())
for i in range(num):
    for j in range(num):
        if len(words[j]) > len(words[i]):
            words[j], words[i] = words[i], words[j]
        elif len(words[j]) == len(words[i]) and words[j] > words[i]:
            words[j], words[i] = words[i], words[j]
for word in words:
    print(word)