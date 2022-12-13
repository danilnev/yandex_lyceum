words = input().split()
dict_words = dict()
numbers = []
for word in words:
    if word not in dict_words.keys():
        dict_words[word] = 1
    else:
        dict_words[word] += 1
    numbers.append(str(dict_words[word]))
print(' '.join(numbers))
