from swift import words
import random


words_lists = dict()
for word in words:
    if word not in words_lists:
        words_lists[word] = []
        for i in range(len(words) - 1):
            if words[i] == word:
                words_lists[word].append(words[i + 1])
word = random.choice(list(words_lists.keys()))
while not word.isalpha():
    word = random.choice(list(words_lists.keys()))
text = word
for i in range(50):
    new_word = random.choice(words_lists[word])
    while new_word == word:
        new_word = random.choice(words_lists[word])
    if new_word.isalpha() and word != '-':
        text += ' ' + new_word
    else:
        text += new_word
    word = new_word
print(text)
