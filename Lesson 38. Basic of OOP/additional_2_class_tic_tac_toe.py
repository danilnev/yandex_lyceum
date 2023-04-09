import numpy as np


class TicTacToeBoard:
    def __init__(self):
        field = np.empty((3, 3), dtype=str)
        field.fill('-')
        self.board = field
        self.player = 'X'

    def new_game(self):
        field = np.empty((3, 3), dtype=str)
        field.fill('-')
        self.board = field
        self.player = 'X'

    def get_field(self):
        return list(map(lambda x: list(x), self.board))

    def check_field(self):
        for i in range(3):
            if self.board[i, 0] == self.board[i, 1] == self.board[i, 2] != '-':
                return self.board[i, 0]
            if self.board[0, i] == self.board[1, i] == self.board[2, i] != '-':
                return self.board[0, i]
        if self.board[0, 0] == self.board[1, 1] == self.board[2, 2] != '-':
            return self.board[0, 0]
        if self.board[0, 2] == self.board[1, 1] == self.board[2, 0] != '-':
            return self.board[0, 2]
        board = self.board.reshape((1, 9))[0]
        if len(list(filter(lambda x: x == '-', board))) == 0:
            return 'D'

    def make_move(self, row, col):
        row -= 1
        col -= 1
        if self.check_field() is None:
            if self.board[row, col] != '-':
                return f'Клетка {row + 1}, {col + 1} уже занята'
            else:
                if self.player == 'X':
                    self.board[row, col] = 'X'
                    self.player = '0'
                else:
                    self.board[row, col] = '0'
                    self.player = 'X'
                result = self.check_field()
                if result == 'X':
                    return 'Победил игрок X'
                elif result == '0':
                    return 'Победил игрок 0'
                elif result == 'D':
                    return 'Ничья'
                else:
                    return 'Продолжаем играть'
        else:
            return 'Игра уже завершена'


board = TicTacToeBoard()
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(board.make_move(1, 2))
print(*board.get_field(), sep="\n")
print(board.make_move(2, 1))
print(board.make_move(2, 2))
print(board.make_move(3, 1))
print(board.make_move(2, 2))
print(*board.get_field(), sep="\n")
