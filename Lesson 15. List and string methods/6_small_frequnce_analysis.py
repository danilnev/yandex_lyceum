word = ''.join(input().lower().split())
maxx = 0
letters = set(word)
for letter in letters:
    if word.count(letter) > maxx:
        maxx = word.count(letter)
        max_letter = letter
    elif word.count(letter) == maxx and letter < max_letter:
        max_letter = letter
print(max_letter)
