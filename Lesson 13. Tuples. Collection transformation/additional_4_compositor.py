string = input()
english = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
russian = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
letters = set()
for letter in string:
    if letter in english:
        for i in range(len(english)):
            if english[i] == letter:
                count = i
        letters.add((letter, count + 1))
    elif letter in russian:
        for i in range(len(russian)):
            if russian[i] == letter:
                count = i
        letters.add((letter, count + 1))
for letter in letters:
    print(letter)
