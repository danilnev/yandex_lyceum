strings = {'true': 0, 'half_true': 0, 'false': 0}
string = input()
while string != 'Final':
    if 'not' in string:
        strings['true'] += len(string)
    elif len(string) <= 20:
        strings['half_true'] += len(string)
    else:
        strings['false'] += len(string)
    string = input()
print(' '.join([str(length) for length in strings.values()]))
