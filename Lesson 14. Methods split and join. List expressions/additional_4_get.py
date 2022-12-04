link = input()
search_key = input()
get = link.split('?')[1]
key_values = [(key_value.split('=')[0], key_value.split('=')[1]) for key_value in get.split('&')]
for key_value in key_values:
    if key_value[0] == search_key:
        print(key_value[1])
        break
