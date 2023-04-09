class Polynomial:
    def __init__(self, coefs):
        self.cfs = coefs

    def __call__(self, x):
        y = self.cfs[0]
        for i, c in enumerate(self.cfs[1:], 1):
            y += c * (x ** i)
        return y

    def __add__(self, oth):
        if len(self.cfs) < len(oth.cfs):
            a = list(map(lambda x: self.cfs[x] + oth.cfs[x] if x < len(self.cfs) else oth.cfs[x], range(len(oth.cfs))))
            return Polynomial(a)
        elif len(self.cfs) > len(oth.cfs):
            a = list(map(lambda x: self.cfs[x] + oth.cfs[x] if x < len(oth.cfs) else self.cfs[x], range(len(self.cfs))))
            return Polynomial(a)
        else:
            return Polynomial(list(map(lambda x: self.cfs[x] + oth.cfs[x], range(len(self.cfs)))))
