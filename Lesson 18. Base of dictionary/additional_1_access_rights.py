num1 = int(input())
ways = [input() for i in range(num1)]
num2 = int(input())
results = []
for i in range(num2):
    search = input()
    add = ''
    for way in ways:
        if way in search and search.find(way) == 0:
            add = 'YES'
            break
        else:
            add = 'NO'
    results.append(add)
print('\n'.join(results))
