arr1 = set()
arr2 = set()
while True:
    element = input()
    if element == '':
        break
    else:
        arr1.add(int(element))
while True:
    element = input()
    if element == '':
        break
    else:
        arr2.add(int(element))
arr3 = arr1.intersection(arr2)
if len(arr3) == 0:
    print('EMPTY')
else:
    for num in arr3:
        print(num)