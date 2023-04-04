class AmericanDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def set_year(self, year):
        self.year = year

    def set_month(self, month):
        self.month = month

    def set_day(self, day):
        self.day = day

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def format(self):
        date = []
        if self.month < 10:
            date.append('0' + str(self.month))
        else:
            date.append(str(self.month))
        if self.day < 10:
            date.append('0' + str(self.day))
        else:
            date.append(str(self.day))
        date.append(str(self.year))
        return '.'.join(date)


class EuropeanDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def set_year(self, year):
        self.year = year

    def set_month(self, month):
        self.month = month

    def set_day(self, day):
        self.day = day

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def format(self):
        date = []
        if self.day < 10:
            date.append('0' + str(self.day))
        else:
            date.append(str(self.day))
        if self.month < 10:
            date.append('0' + str(self.month))
        else:
            date.append(str(self.month))
        date.append(str(self.year))
        return '.'.join(date)
