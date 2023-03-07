def linear(some_list):
    if not some_list:
        return some_list
    if type(some_list[0]) is list:
        return linear(some_list[0]) + linear(some_list[1:])
    return some_list[:1] + linear(some_list[1:])


num = int(input())
words = sorted([input().lower() for i in range(num)])
result = dict()
for word in words:
    anogram = set(filter(lambda x: x != word and set(x) == set(word), words))
    if word not in linear(list(result.values())):
        result[word] = list(anogram)
    else:
        for key in filter(lambda x: result[x] != word and set(result[x]) == set(word), result):
            result[key].append(word)
print(*list(map(lambda x: ' '.join(sorted([x] + result[x])), result)), sep='\n')
