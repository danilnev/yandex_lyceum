num = int(input())
for i in range(num):
    string_result = ''
    string = input()
    i = 0
    while i < len(string):
        if i == 0 and string[i] == ' ':
            while string[i] == ' ':
                i += 1
                string_result += ' '
        if i > 0 and string[i] == ' ':
            while string[i] == ' ':
                i += 1
            string_result += ' '
        elif string[i] == '#':
            break
        elif string[i] == "'":
            string_result += string[i]
            i += 1
            while string[i] != "'":
                if string[i] == '\\':
                    string_result += string[i] + string[i + 1]
                    i += 2
                else:
                    string_result += string[i]
                    i += 1
            string_result += string[i]
            i += 1
        else:
            string_result += string[i]
            i += 1
    print(string_result)