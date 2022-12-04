num_strings = int(input())
search_word = input()
count = 0
for i in range(num_strings):
    string = input()
    if search_word in string or 'забыл' in string:
        count += 1
if count <= num_strings // 2:
    print('НЕ ТАК И МНОГО', count + num_strings, sep='\n')
else:
    print('ВСЕ РАВНО НИЧЕГО СТРАШНОГО', count + num_strings, sep='\n')
