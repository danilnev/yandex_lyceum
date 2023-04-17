class Knight:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def can_move(self, row1, col1):
        return ((self.row - 2, self.col + 1) == (row1, col1) or
                (self.row - 1, self.col + 2) == (row1, col1) or
                (self.row + 1, self.col + 2) == (row1, col1) or
                (self.row + 2, self.col + 1) == (row1, col1) or
                (self.row + 2, self.col - 1) == (row1, col1) or
                (self.row + 1, self.col - 2) == (row1, col1) or
                (self.row - 1, self.col - 2) == (row1, col1) or
                (self.row - 2, self.col - 1) == (row1, col1)) and 0 <= row1 <= 7 and 0 <= col1 <= 7

    def set_position(self, row1, col1):
        self.row = row1
        self.col = col1

    def get_color(self):
        return self.color

    def char(self):
        return 'N'
