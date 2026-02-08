from constaints import *
from engine.Pieces import *

class Board:
    def __init__(self):
        self.board = [[0 for _ in range(DIMENSION)] for _ in range(DIMENSION)]
        self.white_to_move = True
        self.setup_board()

    def setup_board(self):
        i = 0
        pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for col in range(DIMENSION):
            self.board[1][col] = Pawn('b', (1, col))
            self.board[6][col] = Pawn('w', (1, col))

        for piece in pieces:
            self.board[7][i] = piece("w", (7, i))
            self.board[0][i] = piece("b", (0, i))
            i += 1
