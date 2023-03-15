m = int(input())
n = int(input())
k = int(input())
arr = set()
arr_of_good = set()
for i in range(m + n + k):
    element = input()
    if element in arr and element not in arr_of_good:
        arr_of_good.add(element)
        continue
    elif element in arr_of_good:
        arr_of_good.discard(element)
    arr.add(element)
if len(arr_of_good) == 0:
    print('NO')
else:
    print(len(arr_of_good))