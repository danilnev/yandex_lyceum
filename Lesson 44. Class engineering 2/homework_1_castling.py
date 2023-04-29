WHITE = 1
BLACK = 2


def opponent(color):  # Функция, возвращающая противоположный цвет
    if color == WHITE:
        return BLACK
    else:
        return WHITE


def print_board(board):  # Распечатать доску в текстовом виде
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
    board.field[0][0] = Rook(WHITE)
    board.field[0][4] = King(WHITE)
    board.field[0][7] = Rook(WHITE)

    board.field[7][0] = Rook(BLACK)
    board.field[7][4] = King(BLACK)
    board.field[7][7] = Rook(BLACK)

    board.field[0][1] = Knight(WHITE)
    board.field[0][5] = Bishop(WHITE)

    board.field[7][1] = Knight(BLACK)
    board.field[7][5] = Bishop(BLACK)

    print('before:')
    for row in range(7, -1, -1):
        for col in range(8):
            char = board.cell(row, col)[1]
            print(char.replace(' ', '-'), end='')
        print()
    print()

    print("Попыки рокировки с мешающими фигурами")
    print(board.castling0())
    print(board.castling7())

    for row in range(7, -1, -1):
        for col in range(8):
            char = board.cell(row, col)[1]
            print(char.replace(' ', '-'), end='')
        print()
    print()


def correct_coords(row, col):  # Функция определяет, лежат ли координаты внутри доски
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

    def cell(self, row, col):  # Возвращает строку '<color><figure>' или '  ' если в клетке пусто
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

    def move_piece(self, row, col, row1, col1):  # Перемещает фигуру и возвращает True или False (смотря на результат)
        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False
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
        self.field[row][col] = None
        self.field[row1][col1] = piece
        self.color = opponent(self.color)
        if isinstance(piece, (King, Rook)):
            piece.moves = True
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

    def castling0(self):
        if self.color == BLACK:
            rook, king = self.field[7][0], self.field[7][4]
            if not (isinstance(rook, Rook) and isinstance(king, King)):
                return False
            if not rook.can_move(self, 7, 0, 7, 3):
                return False
            if rook.moves or king.moves:
                return False
            self.field[7][0], self.field[7][4] = None, None
            self.field[7][3], self.field[7][2] = rook, king
            self.color = opponent(self.color)
            return True
        else:
            rook, king = self.field[0][0], self.field[0][4]
            if not (isinstance(rook, Rook) and isinstance(king, King)):
                return False
            if not rook.can_move(self, 0, 0, 0, 3):
                return False
            if rook.moves or king.moves:
                return False
            self.field[0][0], self.field[0][4] = None, None
            self.field[0][3], self.field[0][2] = rook, king
            self.color = opponent(self.color)
            return True

    def castling7(self):
        if self.color == BLACK:
            rook, king = self.field[7][7], self.field[7][4]
            if not (isinstance(rook, Rook) and isinstance(king, King)):
                return False
            if not rook.can_move(self, 7, 7, 7, 5):
                return False
            if rook.moves or king.moves:
                return False
            self.field[7][7], self.field[7][4] = None, None
            self.field[7][5], self.field[7][6] = rook, king
            self.color = opponent(self.color)
            return True
        else:
            rook, king = self.field[0][7], self.field[0][4]
            if not (isinstance(rook, Rook) and isinstance(king, King)):
                return False
            if not rook.can_move(self, 0, 7, 0, 5):
                return False
            if rook.moves or king.moves:
                return False
            self.field[0][7], self.field[0][4] = None, None
            self.field[0][5], self.field[0][6] = rook, king
            self.color = opponent(self.color)
            return True


class Rook:
    def __init__(self, color):
        self.color = color
        self.moves = False

    def get_color(self):
        return self.color

    def char(self):
        return 'R'

    def can_move(self, board, row, col, row1, col1, not_with_attack=True):
        if row != row1 and col != col1:
            return False
        if not_with_attack and not board.field[row1][col1] is None:
            return False
        step = 1 if (row1 >= row) else -1
        for r in range(row + step, row1, step):  # Есть ли по горизонтали фигуры на пути
            if not (board.get_piece(r, col) is None):
                return False
        step = 1 if (col1 >= col) else -1
        for c in range(col + step, col1, step):  # Есть ли по вертикали фигуры на пути
            if not (board.get_piece(row, c) is None):
                return False
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1, not_with_attack=False)


class Pawn:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'P'

    def can_move(self, board, row, col, row1, col1):
        if col != col1:
            return False
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6
        if row + direction == row1:  # ход на 1 клетку
            return True
        if (row == start_row  # ход на 2 клетки из начального положения
                and row + 2 * direction == row1
                and board.field[row + direction][col] is None):
            return True
        return False

    def can_attack(self, board, row, col, row1, col1):
        direction = 1 if (self.color == WHITE) else -1
        return (row + direction == row1
                and (col + 1 == col1 or col - 1 == col1))


class Knight:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'N'  # kNight, буква 'K' уже занята королём

    def can_move(self, board, row, col, row1, col1):
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)


class King:
    def __init__(self, color):
        self.color = color
        self.moves = False

    def get_color(self):
        return self.color

    def char(self):
        return 'K'

    def can_move(self, board, row, col, row1, col1):
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)


class Queen:
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
            for r in range(row + step, row1, step):  # есть ли мешающие фигуры по горизонтали
                if not (board.get_piece(r, col) is None):
                    return False
            return True
        if row == row1 and col != col1:
            step = 1 if (col1 >= col) else -1
            for c in range(col + step, col1, step):  # есть ли мешающие фигуры по вертикали
                if not (board.get_piece(row, c) is None):
                    return False
            return True
        return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)


class Bishop:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'B'

    def can_move(self, board, row, col, row1, col1):
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)


if __name__ == "__main__":
    main()
