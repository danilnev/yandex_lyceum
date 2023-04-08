class Summator:
    def transform(self, n):
        return n

    def sum(self, N):
        return sum(map(lambda x: self.transform(x), range(1, N + 1)))


class SquareSummator(Summator):
    def transform(self, n):
        return n ** 2


class CubeSummator(Summator):
    def transform(self, n):
        return n ** 3
