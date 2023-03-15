num_of_boxes = int(input())
arr1 = set()
arr2 = set()
count = 0
for i in range(num_of_boxes):
    num = int(input())
    for i in range(num):
        element = input()
        if element in arr1 and element not in arr2:
            count += 2
            arr2.add(element)
        elif element not in arr1:
            arr1.add(element)
        else:
            count += 1
print(len(arr2), count)