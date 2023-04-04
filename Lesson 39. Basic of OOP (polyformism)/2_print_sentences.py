class LeftParagraph:
    def __init__(self, max_length):
        self.max_length = max_length
        self.strings = []

    def add_word(self, word):
        if not self.strings or len(self.strings[-1]) + len(word) + 1 > self.max_length:
            self.strings.append(word)
        else:
            self.strings[-1] += ' ' + word

    def end(self):
        print(*self.strings, sep='\n')
        self.strings = []


class RightParagraph:
    def __init__(self, max_length):
        self.max_length = max_length
        self.strings = []

    def add_word(self, word):
        if not self.strings or len(self.strings[-1]) + len(word) + 1 > self.max_length:
            self.strings.append(word)
        else:
            self.strings[-1] += ' ' + word

    def end(self):
        print(*map(lambda x: ' ' * (self.max_length - len(x)) + x, self.strings), sep='\n')
        self.strings = []
