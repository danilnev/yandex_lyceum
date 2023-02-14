import itertools


dictionary = list(map(str.lower, input().split()))
text = input().split()
result = []
for word in text:
    types = set(itertools.permutations(list(word.lower())))
    if len(set(map(''.join, types)).intersection((set(dictionary) - {word.lower()}))) >= 1:
        result.append('#' * len(word))
    else:
        result.append(word.lower())
print(*result)
