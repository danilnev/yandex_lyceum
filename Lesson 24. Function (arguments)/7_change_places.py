value = 3
addition = 5
print('id =', id(value))
value = value + addition
print(value, 'id =', id(value))
value = 3
addition = 5
print('id =', id(value))
value += addition
print(value, 'id =', id(value))
print('Вывод: в случае с числами различия нет.\n')

value = 'Hello'
addition = 'Yandex'
print('id =', id(value))
value = value + addition
print(value, 'id =', id(value))
value = 'Hello'
addition = 'Yandex'
print('id =', id(value))
value += addition
print(value, 'id =', id(value))
print('Вывод: в случае со строками различаются id в конечных результатах.\n')

value = [1, 2, 3]
addition = [4, 5, 6]
print('id =', id(value))
value = value + addition
print(value, 'id =', id(value))
value = [1, 2, 3]
addition = [4, 5, 6]
print('id =', id(value))
value += addition
print(value, 'id =', id(value))
print('Вывод: в случае со списками различаются id в конечных результатах.')
