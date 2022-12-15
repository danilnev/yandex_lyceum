num = int(input())
words = dict()
text = list()
for i in range(num):
    string = input().split()
    for j in range(len(string)):
        word = string[j]
        new_word = ''
        if not word.isalpha():
            for symbol in word:
                if symbol.isalpha():
                    new_word += symbol
        else:
            new_word = word
        string[j] = new_word.capitalize()
    text = text + string
for word in text:
    if word not in words:
        words[word] = text.count(word)
for i in range(len(words)):
    maxx = max(words.values())
    array = []
    for word in words.keys():
        if words[word] == maxx:
            array.append(word)
    array.sort()
    print(array[0])
    words.pop(array[0])
