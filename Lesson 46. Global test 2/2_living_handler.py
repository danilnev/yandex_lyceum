def conversions(*strings):
    magic = dict()
    for string in strings:
        string = string.split()
        if string[-1] not in magic:
            magic[string[-1]] = []
        magic[string[-1]].append(string[0].capitalize())
        magic[string[-1]].sort(reverse=True)
    return magic


data = [
    'clouds blanket',
    'crows in the morning alarm clock',
    'snow in a fluffy blanket',
    'fog in a light blanket'
]
print(conversions(*data))
