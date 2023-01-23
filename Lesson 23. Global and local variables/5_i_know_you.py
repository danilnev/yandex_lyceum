def polite_input(question):
    global name
    if name == '':
        name = input('Как вас зовут?\n')
    return input(f'{name}, {question}\n')


name = ''
# age = polite_input('укажите возраст')
# school_number = polite_input('укажите номер школы')
# class_num = polite_input('укажите полный номер класса')
# print(f'Name -', name, '\nAge -', age, '\nSchool -', school_number, '\nClass -', class_num)
