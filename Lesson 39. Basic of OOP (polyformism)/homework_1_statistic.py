class MinStat:
    def __init__(self):
        self.numbers = []

    def add_number(self, num):
        self.numbers.append(num)

    def result(self):
        if self.numbers:
            return min(self.numbers)
        else:
            return None


class MaxStat:
    def __init__(self):
        self.numbers = []

    def add_number(self, num):
        self.numbers.append(num)

    def result(self):
        if self.numbers:
            return max(self.numbers)
        else:
            return None


class AverageStat:
    def __init__(self):
        self.numbers = []

    def add_number(self, num):
        self.numbers.append(num)

    def result(self):
        if self.numbers:
            return sum(self.numbers) / len(self.numbers)
        else:
            return None
