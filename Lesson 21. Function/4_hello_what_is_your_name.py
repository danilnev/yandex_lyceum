def who_are_you_and_hello():
    while True:
        name = input()
        if ' ' not in name and name.isalpha() and name[0].isupper() and name[1:].islower():
            break
    print(f'Привет, {name}!')


# who_are_you_and_hello()
