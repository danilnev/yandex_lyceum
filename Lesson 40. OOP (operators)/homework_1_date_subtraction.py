import datetime


class Date:
    def __init__(self, month, day):
        self.date = datetime.date(year=2022, month=month, day=day)

    def __sub__(self, other):
        return (self.date - other.date).days
