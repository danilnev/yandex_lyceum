class Table:
    def __init__(self, rows, cols):
        self.table = [[0 for i in range(rows)] for j in range(cols)]
        self.rows = rows
        self.cols = cols

    def get_value(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.table[col][row]
        else:
            return None

    def set_value(self, row, col, value):
        self.table[col][row] = value

    def n_rows(self):
        return self.rows

    def n_cols(self):
        return self.cols
