m = int(input())
n = int(input())
arr = set()
for i in range(n + m):
    element = input()
    if element in arr:
        arr.discard(element)
    else:
        arr.add(element)
if len(arr) == 0:
    print('NO')
else:
    print(len(arr))