class MinMaxWordFinder:
    def __init__(self):
        self.words = []

    def add_sentence(self, sentence):
        self.words += sentence.split()

    def shortest_words(self):
        if self.words:
            length = len(min(self.words, key=lambda x: len(x)))
            return sorted(list(filter(lambda x: len(x) == length, self.words)))
        else:
            return ''

    def longest_words(self):
        if self.words:
            length = len(max(self.words, key=lambda x: len(x)))
            return sorted(list(set(filter(lambda x: len(x) == length, self.words))))
        else:
            return ''
