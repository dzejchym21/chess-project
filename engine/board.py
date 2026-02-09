from constaints import *
from engine.pieces import *

class Board:
    def __init__(self):
        self.board = [[0 for _ in range(DIMENSION)] for _ in range(DIMENSION)]
        self.white_to_move = True
        self.setup_board()
        print(self.board)

    def setup_board(self):
        i = 0
        pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for col in range(DIMENSION):
            self.board[1][col] = Pawn('b', (1, col))
            self.board[6][col] = Pawn('w', (6, col))

        for piece in pieces:
            self.board[7][i] = piece("w", (7, i))
            self.board[0][i] = piece("b", (0, i))
            i += 1

    def make_move(self, sq_from, sq_to):
        s_row, s_col = sq_from
        e_row, e_col = sq_to

        piece = self.board[s_row][s_col]
        if piece != 0:
            valid_moves = piece.get_valid_moves(self.board)
            if (e_row, e_col) in valid_moves:
                self.board[e_row][e_col] = piece
                piece.pos = (e_row, e_col)
                self.board[s_row][s_col] = 0
                self.white_to_move = not self.white_to_move

    def get_piece(self, row, col):
        return self.board[row][col]

    def get_board(self):
        return self.board