num = int(input())
arr = set()
for i in range(num):
    arr.add(input())
if input() in arr:
    print('TRY ANOTHER')
else:
    print('OK')