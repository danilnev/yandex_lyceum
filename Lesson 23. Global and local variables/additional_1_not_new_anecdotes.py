def print_only_new(message):
    global anecdotes
    if message not in anecdotes:
        print(message)
        anecdotes.append(message)


anecdotes = []
# print_only_new('Шутка номер 15')
# print_only_new('Шутка номер 23')
# print_only_new('Шутка номер 24')
# print_only_new('Шутка номер 24')
# print_only_new('Шутка номер 100')
# print_only_new('Шутка номер 24')
# print_only_new('Шутка номер 99')
# print_only_new('Шутка номер 15')
# print_only_new('Шутка номер 100')
