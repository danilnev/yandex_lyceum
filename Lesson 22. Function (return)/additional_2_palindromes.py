def palindrome(s: str) -> str:
    string = ''.join(s.lower().split())
    reverse_string = ''.join(reversed(list(string)))
    if string == reverse_string:
        return 'Палиндром'
    else:
        return 'Не палиндром'


# print(palindrome('А роза упала на лапу Азора'))
# print(palindrome('Палиндром'))
