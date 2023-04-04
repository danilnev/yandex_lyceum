class Table:
    def __init__(self, rows, cols):
        self.table = [[0 for i in range(cols)] for j in range(rows)]
        self.row = rows
        self.col = cols

    def get_value(self, row, col):
        if 0 <= row < self.row and 0 <= col < self.col:
            return self.table[row][col]
        else:
            return None

    def set_value(self, row, col, val):
        self.table[row][col] = val

    def n_rows(self):
        return self.row

    def n_cols(self):
        return self.col

    def delete_row(self, row):
        self.table.pop(row)
        self.col -= 1

    def delete_col(self, col):
        for index in range(self.col):
            self.table[index].pop(col)
        self.col -= 1

    def add_row(self, row):
        self.table.insert(row, [0 for i in range(self.col)])
        self.row += 1

    def add_col(self, col):
        for index in range(self.row):
            self.table[index].insert(col, 0)
        self.col += 1



