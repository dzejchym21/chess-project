from constaints import *

class Board:
    def __init__(self):
        self.board = [[0 for _ in range(DIMENSION)] for _ in range(DIMENSION)]
        self.white_to_move = True

