num_titles = int(input())
titles = []
for i in range(num_titles):
    name = input()
    string = ''
    while name != '*':
        string += ' ' + name
        name = input()
    titles.append('-'.join(string.split()))
titles.reverse()
print(', '.join(titles))
