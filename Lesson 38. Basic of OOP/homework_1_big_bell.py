class BigBell:
    def __init__(self):
        self.ding = True

    def sound(self):
        if self.ding:
            print('ding')
        else:
            print('dong')
        self.ding = not self.ding
