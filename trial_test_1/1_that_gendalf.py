num_symbols = 0
string = input()
while 'Гэндальф' not in string:
    if 'волшебн' in string:
        num_symbols += len(string)
    string = input()
print(num_symbols)
