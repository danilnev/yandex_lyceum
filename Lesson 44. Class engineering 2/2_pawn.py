WHITE = 1
BLACK = 2


# Удобная функция для вычисления цвета противника
def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE


def print_board(board):  # Распечатать доску в текстовом виде (см. скриншот)
    print('     +----+----+----+----+----+----+----+----+')
    for row in range(7, -1, -1):
        print(' ', row, end='  ')
        for col in range(8):
            print('|', board.cell(row, col), end=' ')
        print('|')
        print('     +----+----+----+----+----+----+----+----+')
    print(end='        ')
    for col in range(8):
        print(col, end='    ')
    print()


def main():
    board = Board()
    board.field = [([None] * 8) for i in range(8)]
    board.field[6][0] = Pawn(WHITE)
    board.field[6][1] = Pawn(WHITE)
    board.field[6][3] = Pawn(WHITE)
    board.field[6][4] = Pawn(WHITE)

    board.field[1][1] = Pawn(BLACK)
    board.field[1][4] = Pawn(BLACK)
    board.field[1][5] = Pawn(BLACK)
    board.field[1][7] = Pawn(BLACK)

    print('before:')
    for row in range(7, -1, -1):
        for col in range(8):
            char = board.cell(row, col)[1]
            print(char.replace(' ', '-'), end='')
        print()
    print()

    board.move_and_promote_pawn(6, 0, 7, 0, 'Q')
    board.move_and_promote_pawn(1, 1, 0, 1, 'R')

    board.move_and_promote_pawn(6, 1, 7, 1, 'N')
    board.move_and_promote_pawn(1, 4, 0, 4, 'Q')

    board.move_and_promote_pawn(6, 3, 7, 3, 'B')
    board.move_and_promote_pawn(1, 5, 0, 5, 'N')

    board.move_and_promote_pawn(6, 4, 7, 4, 'R')
    board.move_and_promote_pawn(1, 7, 0, 7, 'B')

    print('8 turns after:')
    for row in range(7, -1, -1):
        for col in range(8):
            char = board.cell(row, col)[1]
            print(char.replace(' ', '-'), end='')
        print()


def correct_coords(row, col):
    '''Функция проверяет, что координаты (row, col) лежат
    внутри доски'''
    return 0 <= row < 8 and 0 <= col < 8


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)
        self.field[0] = [
            Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
            King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)
        ]
        self.field[1] = [
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE),
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)
        ]
        self.field[6] = [
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK),
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)
        ]
        self.field[7] = [
            Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
            King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)
        ]

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        '''Возвращает строку из двух символов. Если в клетке (row, col)
        находится фигура, символы цвета и фигуры. Если клетка пуста,
        то два пробела.'''
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def get_piece(self, row, col):
        if correct_coords(row, col):
            return self.field[row][col]
        else:
            return None

    def move_piece(self, row, col, row1, col1):
        '''Переместить фигуру из точки (row, col) в точку (row1, col1).
        Если перемещение возможно, метод выполнит его и вернёт True.
        Если нет --- вернёт False'''

        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False  # нельзя пойти в ту же клетку
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if self.field[row1][col1] is None:
            if not piece.can_move(self, row, col, row1, col1):
                return False
        elif self.field[row1][col1].get_color() == opponent(piece.get_color()):
            if not piece.can_attack(self, row, col, row1, col1):
                return False
        else:
            return False
        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        self.color = opponent(self.color)
        return True

    def move_and_promote_pawn(self, row, col, row1, col1, char):
        figures = {'Q': Queen, 'R': Rook, 'B': Bishop, 'N': Knight}
        piece = self.field[row][col]
        if not isinstance(piece, Pawn):
            return False
        color = self.field[row][col].get_color()
        if (piece.can_move(self, row, col, row1, col1) and self.field[row1][col1] is None) or \
                (piece.can_attack(self, row, col, row1, col1) and
                 (not self.field[row1][col1] is None) and
                 self.field[row1][col1].get_color() != color):
            self.field[row][col] = None
            self.field[row1][col1] = figures[char](color)
            self.color = opponent(color)
            return True
        return False


class Rook:

    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'R'

    def can_move(self, board, row, col, row1, col1):
        # Невозможно сделать ход в клетку, которая не лежит в том же ряду
        # или столбце клеток.
        if row != row1 and col != col1:
            return False

        step = 1 if (row1 >= row) else -1
        for r in range(row + step, row1, step):
            # Если на пути по горизонтали есть фигура
            if not (board.get_piece(r, col) is None):
                return False

        step = 1 if (col1 >= col) else -1
        for c in range(col + step, col1, step):
            # Если на пути по вертикали есть фигура
            if not (board.get_piece(row, c) is None):
                return False

        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Pawn:

    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'P'

    def can_move(self, board, row, col, row1, col1):
        # Пешка может ходить только по вертикали
        # "взятие на проходе" не реализовано
        if col != col1:
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
        if row + direction == row1:
            return True

        # ход на 2 клетки из начального положения
        if (row == start_row
                and row + 2 * direction == row1
                and board.field[row + direction][col] is None):
            return True

        return False

    def can_attack(self, board, row, col, row1, col1):
        direction = 1 if (self.color == WHITE) else -1
        return (row + direction == row1
                and (col + 1 == col1 or col - 1 == col1))


class Knight:
    '''Класс коня. Пока что заглушка, которая может ходить в любую клетку.'''

    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'N'  # kNight, буква 'K' уже занята королём

    def can_move(self, board, row, col, row1, col1):
        return True  # Заглушка

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)


class King:
    '''Класс короля. Пока что заглушка, которая может ходить в любую клетку.'''

    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'K'

    def can_move(self, board, row, col, row1, col1):
        return True  # Заглушка

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)


class Queen:
    '''Класс ферзя. Пока что заглушка, которая может ходить в любую клетку.'''

    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'Q'

    def can_move(self, board, row, col, row1, col1):
        if not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False
        if not (board.get_piece(row1, col1) is None):
            if board.get_piece(row1, col1).get_color() == board.get_piece(row, col).get_color():
                return False
        if row - col == row1 - col1:
            step = 1 if row1 > row else -1
            for i in range(row + step, row1, step):
                c = i - (row - col)
                if not (board.get_piece(i, c) is None):
                    return False
            return True
        if row + col == row1 + col1:
            step = 1 if row1 > row else -1
            for i in range(row + step, row1, step):
                c = (row + col) - i
                if not (board.get_piece(i, c) is None):
                    return False
            return True
        if row != row1 and col == col1:
            step = 1 if (row1 >= row) else -1
            for r in range(row + step, row1, step):
                # Если на пути по горизонтали есть фигура
                if not (board.get_piece(r, col) is None):
                    return False
            return True
        if row == row1 and col != col1:
            step = 1 if (col1 >= col) else -1
            for c in range(col + step, col1, step):
                # Если на пути по вертикали есть фигура
                if not (board.get_piece(row, c) is None):
                    return False
            return True
        return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)


class Bishop:
    '''Класс слона. Пока что заглушка, которая может ходить в любую клетку.'''

    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'B'

    def can_move(self, board, row, col, row1, col1):
        return True  # Заглушка

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)


if __name__ == "__main__":
    main()
