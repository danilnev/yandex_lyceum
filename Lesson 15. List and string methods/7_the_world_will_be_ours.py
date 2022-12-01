words = input().upper().split()
for i in range(len(words)):
    words[i] = '-'.join(list(words[i]))
print(' '.join(words))
