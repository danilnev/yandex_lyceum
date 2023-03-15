word = input()
count = 0
maxx = 0
for letter in word:
    if letter == 'о':
        count += 1
    else:
        if count > maxx:
            maxx = count
        count = 0
if count > maxx:
    maxx = count
print(maxx)