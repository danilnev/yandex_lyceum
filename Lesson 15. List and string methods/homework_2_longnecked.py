string = input().lower()
letters = set(string)
lengths = [string.count(letter) for letter in letters]
print(max(lengths))
