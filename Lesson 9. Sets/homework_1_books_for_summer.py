m = int(input())
n = int(input())
arr1 = set()
for i in range(m):
    arr1.add(input())
for i in range(n):
    element = input()
    if element in arr1:
        print('YES')
    else:
        print('NO')