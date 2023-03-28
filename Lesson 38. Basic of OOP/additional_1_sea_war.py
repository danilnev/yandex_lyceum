import numpy as np


class SeaMap:
    def __init__(self):
        array = np.empty((12, 12), dtype=str)
        array.fill('.')
        self.field = array

    def shoot(self, row, col, res):
        if res == 'miss':
            self.field[row + 1, col + 1] = '*'
        elif res == 'hit':
            self.field[row + 1, col + 1] = 'x'
        else:
            self.field[row + 1, col + 1] = 'x'
            i = 1
            while (row + 1 - i) >= 0 and self.field[row + 1 - i, col + 1] == 'x':
                self.field[row + 1 - i, col + 1 - 1] = '*'
                self.field[row + 1 - i, col + 1 + 1] = '*'
                i += 1
            self.field[row + 1 - i, col + 1 - 1] = '*'
            self.field[row + 1 - i, col + 1] = '*'
            self.field[row + 1 - i, col + 1 + 1] = '*'

            i = 1
            while (row + 1 + i) <= 9 and self.field[row + 1 + i, col + 1] == 'x':
                self.field[row + 1 + i, col + 1 - 1] = '*'
                self.field[row + 1 + i, col + 1 + 1] = '*'
                i += 1
            self.field[row + 1 + i, col] = '*'
            self.field[row + 1 + i, col + 1] = '*'
            self.field[row + 1 + i, col + 1 + 1] = '*'

            i = 1
            while (col + 1 - i) >= 0 and self.field[row + 1, col + 1 - i] == 'x':
                self.field[row + 1 - 1, col + 1 - i] = '*'
                self.field[row + 1 + 1, col + 1 - i] = '*'
                i += 1
            self.field[row, col + 1 - i] = '*'
            self.field[row + 1, col + 1 - i] = '*'
            self.field[row + 1 + 1, col + 1 - i] = '*'

            i = 1
            while (col + 1 + i) <= 9 and self.field[row + 1, col + 1 + i] == 'x':
                self.field[row + 1 - 1, col + 1 + i] = '*'
                self.field[row + 1 + 1, col + 1 + i] = '*'
                i += 1
            self.field[row, col + 1 + i] = '*'
            self.field[row + 1, col + 1 + i] = '*'
            self.field[row + 1 + 1, col + 1 + i] = '*'

    def cell(self, row, col):
        return self.field[row + 1, col + 1]


sm = SeaMap()

sm.shoot(0, 0, 'hit')
sm.shoot(0, 1, 'sink')

sm.shoot(9, 8, 'hit')
sm.shoot(9, 9, 'sink')

sm.shoot(2, 3, 'sink')

sm.shoot(5, 6, 'miss')
sm.shoot(7, 8, 'miss')
sm.shoot(1, 7, 'miss')

sm.shoot(1, 7, 'miss')

for row in range(10):
    for col in range(10):
        print(sm.cell(row, col), end='')
    print()
