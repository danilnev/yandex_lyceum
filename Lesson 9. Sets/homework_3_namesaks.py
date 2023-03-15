n = int(input())
arr = set()
arr_result = set()
count = 0
for i in range(n):
    element = input()
    if element not in arr:
        arr.add(element)
    elif element in arr and element in arr_result:
        count += 1
    else:
        count += 2
        arr_result.add(element)
print(count)
