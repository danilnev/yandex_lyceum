def correct_coords(row, col):
    """Функция проверяет, что координаты (row, col) лежат
    внутри доски"""
    return 0 <= row < 8 and 0 <= col < 8


def opponent(color):
    if color == WHITE:
        return BLACK
    return WHITE


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)
        # Пешка белого цвета в клетке E2.
        self.field[1][4] = Pawn(1, 4, WHITE)

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        """Возвращает строку из двух символов. Если в клетке (row, col)
        находится фигура, символы цвета и фигуры. Если клетка пуста,
        то два пробела."""
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def move_piece(self, row, col, row1, col1):
        """Переместить фигуру из точки (row, col) в точку (row1, col1).
        Если перемещение возможно, метод выполнит его и вернет True.
        Если нет --- вернет False"""

        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False  # нельзя пойти в ту же клетку
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if not piece.can_move(row1, col1):
            return False
        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        piece.set_position(row1, col1)
        self.color = opponent(self.color)
        return True

    def is_under_attack(self, row1, col1, color):
        for i in range(len(self.field)):
            row = self.field[i]
            for j in range(len(row)):
                col = row[j]
                if not (col is None):
                    if col.can_move(row1, col1) and col.get_color() == color:
                        return True
        return False


class Rook:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'R'

    def get_color(self):
        return self.color

    def can_move(self, row, col):
        # Невозможно сделать ход в клетку, которая не лежит в том же ряду
        # или столбце клеток.
        if self.row != row and self.col != col:
            return False

        return True


class Pawn:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'P'

    def get_color(self):
        return self.color

    def can_move(self, row, col):
        # Пешка может ходить только по вертикали
        # "взятие на проходе" не реализовано
        if self.col != col:
            return False

        # Пешка может сделать из начального положения ход на 2 клетки
        # вперёд, поэтому поместим индекс начального ряда в start_row.
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        # ход на 1 клетку
        if self.row + direction == row:
            return True

        # ход на 2 клетки из начального положения
        if self.row == start_row and self.row + 2 * direction == row:
            return True

        return False


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


class Bishop:
    def __init__(self, row, col, color):
        self.row, self.col, self.color = row, col, color

    def can_move(self, row1, col1):
        return abs(self.row - row1) == abs(self.col - col1) and 0 <= row1 <= 7 and 0 <= col1 <= 7

    def set_position(self, row1, col1):
        self.row, self.col = row1, col1

    def get_color(self):
        return self.color

    def char(self):
        return 'B'


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


WHITE = 1
BLACK = 2

board = Board()

board.field = [([None] * 8) for i in range(8)]
board.field[0][5] = Rook(0, 5, WHITE)
board.field[1][2] = Bishop(1, 2, WHITE)
board.field[7][6] = Knight(7, 6, BLACK)
w_coords = ((0, 5), (1, 2))
b_coords = ((7, 6), )

print('White:')
for row in range(7, -1, -1):
    for col in range(8):
        if (row, col) in w_coords:
            print('W', end='')
        elif board.is_under_attack(row, col, WHITE):
            print('x', end='')
        else:
            print('-', end='')
    print()
print()

print('Black:')
for row in range(7, -1, -1):
    for col in range(8):
        if (row, col) in b_coords:
            print('B', end='')
        elif board.is_under_attack(row, col, BLACK):
            print('x', end='')
        else:
            print('-', end='')
    print()
