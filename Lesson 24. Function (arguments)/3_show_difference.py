arr1 = [5, 6, 2, 8, 3]
print(f'До использования метода .sort(): {arr1}, id = {id(arr1)}')
print(f'Во время использования метода .sort(): {arr1.sort()}')
print(f'После использования метода .sort(): {arr1}, id = {id(arr1)}')
print()

arr2 = [5, 6, 2, 8, 3]
print(f'До использования функции sorted(): {arr2}, id = {id(arr2)}')
arr3 = sorted(arr2)
print(f'Во время использования функции sorted(): {arr3}')
print(f'После использования функции sorted(): {arr3}, id = {id(arr3)}')
print(f'Прежний список: {arr2}, id = {id(arr2)}')
