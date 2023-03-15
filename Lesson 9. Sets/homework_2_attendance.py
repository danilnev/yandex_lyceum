m = int(input())
arr_last = set()
for i in range(m):
    n = int(input())
    arr = set()
    for i in range(n):
        arr.add(input())
    if len(arr_last) == 0:
        arr_last = arr
    else:
        arr_last = arr_last.intersection(arr)
for elem in arr_last:
    print(elem)