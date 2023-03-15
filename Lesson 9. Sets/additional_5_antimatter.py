arr_last = set()
count = True
deleted = set()
while count:
    arr1 = set()
    while True:
        num = input()
        if num == '':
            count = False
            break
        num = int(num)
        if num == -1:
            break
        else:
            arr1.add(num)
    deleted = deleted.union(arr_last.intersection(arr1))
    arr_last = arr_last.symmetric_difference(arr1) - deleted
for elem in arr_last:
    print(elem, end=' ')