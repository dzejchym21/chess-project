from constaints import *
from engine.Pieces import *

class Board:
    def __init__(self):
        self.board = [[0 for _ in range(DIMENSION)] for _ in range(DIMENSION)]
        self.white_to_move = True
        self.setup_board()

    def setup_board(self):
        for col in range(DIMENSION):
            self.board[1][col] = Pawn('b', (1, col))
            self.board[6][col] = Pawn('w', (1, col))
