def encrypt_caesar(msg: str, shift=3):
    msg = list(msg)
    result = ''
    for symbol in msg:
        if symbol.isalpha():
            if symbol.isupper():
                code = ord(symbol)
                code += shift
                if code < 1040:
                    code = 1071 - (1040 % code) + 1
                elif code > 1071:
                    code = 1040 + (code % 1071) - 1
            elif symbol.islower():
                code = ord(symbol)
                code += shift
                if code < 1072:
                    code = 1103 - (1072 % code) + 1
                elif code > 1103:
                    code = 1072 + (code % 1103) - 1
            result += chr(code)
        else:
            result += symbol
    return result


def decrypt_caesar(msg, shift=3):
    return encrypt_caesar(msg, -shift)


msg = "И не Цезарь, тоже привет."
encrypted = encrypt_caesar(msg, shift=54)
decrypted = decrypt_caesar(encrypted, shift=54)
print(encrypted)
print(decrypted)