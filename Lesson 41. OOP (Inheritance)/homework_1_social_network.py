class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, user, message):
        pass

    def post(self, message):
        pass

    def info(self):
        return ''

    def describe(self):
        print(self.info())


class Person(User):
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def info(self):
        return f'Дата рождения: {self.date}'

    def subscribe(self, user):
        pass


class Community(User):
    def __init__(self, name, about):
        self.name = name
        self.about = about

    def info(self):
        return f'Описание: {self.about}'
