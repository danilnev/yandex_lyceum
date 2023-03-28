class OddEvenSeparator:
    def __init__(self):
        self.odds = []
        self.evens = []

    def add_number(self, num):
        if num % 2 == 0:
            self.evens.append(num)
        else:
            self.odds.append(num)

    def even(self):
        return self.evens

    def odd(self):
        return self.odds
