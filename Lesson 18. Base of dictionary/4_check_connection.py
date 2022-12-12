words = [word.lower() for word in input().split()]
dict_words = dict()
dict_words[words[0]] = 1
print(1, end='')
for word in words[1:]:
    if word not in dict_words.keys():
        dict_words[word] = 1
    else:
        dict_words[word] += 1
    print(' ' + str(dict_words[word]), end='')
