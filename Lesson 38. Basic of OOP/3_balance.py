class Balance:
    def __init__(self):
        self.right = 0
        self.left = 0

    def add_right(self, num):
        self.right += num

    def add_left(self, num):
        self.left += num

    def result(self):
        if self.left == self.right:
            return '='
        elif self.left > self.right:
            return 'L'
        else:
            return 'R'
