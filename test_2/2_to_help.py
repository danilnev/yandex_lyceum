def to_rescue(key, additional='-'):
    global need_help
    words = []
    for word in need_help:
        word = list(set(filter(lambda x: x not in key, list(word))))
        words.append(''.join(sorted(word) + [additional for i in range(len(key) - len(word))]))
    need_help = words
    return
