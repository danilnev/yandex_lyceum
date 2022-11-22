letter_a = [' * ', '* *', '***', '* *', '* *']
letter_b = ['** ', '* *', '** ', '* *', '** ']
letter_c = [' * ', '* *', '*  ', '* *', ' * ']
string = input()
for i in range(5):
    string_print = ''
    for letter in string:
        if letter == 'A':
            string_print += letter_a[i] + '  '
        elif letter == 'B':
            string_print += letter_b[i] + '  '
        else:
            string_print += letter_c[i] + '  '
    print(string_print)
