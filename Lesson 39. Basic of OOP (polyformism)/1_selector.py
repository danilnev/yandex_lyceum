class Selector:
    def __init__(self, numbers):
        self.odds = list(filter(lambda x: x % 2 == 1, numbers))
        self.evens = list(filter(lambda x: x % 2 == 0, numbers))

    def get_evens(self):
        return self.evens

    def get_odds(self):
        return self.odds
