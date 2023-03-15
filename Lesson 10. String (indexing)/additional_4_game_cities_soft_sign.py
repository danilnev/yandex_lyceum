word1 = input()
word2 = input()
if word1[-1] == 'ь' and word1[-2] == word2[0]:
    print('ВЕРНО')
elif word1[-1] == word2[0]:
    print('ВЕРНО')
else:
    print('НЕВЕРНО')