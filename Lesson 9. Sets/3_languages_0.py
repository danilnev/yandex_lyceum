m = int(input())
n = int(input())
arr1 = set()
arr2 = set()
for i in range(m):
    arr1.add(input())
for i in range(n):
    arr2.add(input())
arr3 = arr1.symmetric_difference(arr2)
if len(arr3) == 0:
    print('NO')
else:
    print(len(arr3))