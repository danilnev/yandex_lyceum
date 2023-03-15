step = int(input())
word = input()
string = ''
for letter in word:
    if 1072 <= ord(letter) <= (1103 - step) or 1040 <= ord(letter) <= (1071 - step):
        string += chr(ord(letter) + step)
    elif (1072 - step + 1) <= ord(letter) <= 1103:
        string += chr(1072 + (ord(letter) + step - 1103) - 1)
    elif (1040 - step + 1) <= ord(letter) <= 1071:
        string += chr(1040 + (ord(letter) + step - 1071) - 1)
    else:
        string += letter
print(string)