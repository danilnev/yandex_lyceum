def from_string_to_list(string, container):
    container.extend([int(num) for num in string.split()])


# a = [77, 'abc']
# from_string_to_list("", a)
# print(*a)
