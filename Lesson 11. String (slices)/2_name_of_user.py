name = input()
result = 'OK'
for symbol in name:
    if 'a' <= symbol <= 'z' or '0' <= symbol <= '9' or symbol == '_':
        continue
    else:
        result = 'Неверный символ: ' + symbol
        break
print(result)