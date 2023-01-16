def bracket_check(test_string):
    count = 0
    flag = False
    for letter in test_string:
        if letter == '(':
            count += 1
        elif letter == ')':
            count -= 1
        if count < 0:
            flag = True
            break
    if flag or count != 0:
        print('NO')
    else:
        print('YES')


# bracket_check("()")
# bracket_check("(()((")