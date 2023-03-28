test_string = input().lower()
does = [string for string in input().split(', ')]
set_test = set(test_string)
result = []
for do in does:
    set1 = set(do.lower())
    summ = len(set_test.intersection(set1))
    if summ <= 5:
        result.append(do)
print(' & '.join(result))
