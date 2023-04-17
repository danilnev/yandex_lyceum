class Queen:
    def __init__(self, row, col, color):
        self.row, self.col, self.color = row, col, color

    def can_move(self, row1, col1):
        return (
                abs(self.row - row1) == abs(self.col - col1) or
                self.row == row1 or
                self.col == col1
        ) and 0 <= row1 <= 7 and 0 <= col1 <= 7

    def set_position(self, row1, col1):
        self.row, self.col = row1, col1

    def get_color(self):
        return self.color

    def char(self):
        return 'Q'
