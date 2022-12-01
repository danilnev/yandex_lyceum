number = int(input()[1:])
strings = [input() for i in range(number)]
for string in strings:
    if '#' in string:
        index = string.find('#')
        string = string[:index].rstrip()
    else:
        string = string.rstrip()
    print(string)
