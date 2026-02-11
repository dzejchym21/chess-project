from constaints import *
from engine.pieces import *

class Board:
    def __init__(self):
        self.board = [[0 for _ in range(DIMENSION)] for _ in range(DIMENSION)]
        self.white_to_move = True
        self.setup_board()
        self.black_king_pos = (0, 4)
        self.white_king_pos = (7, 4)
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
            legal_moves = self.get_legal_moves(piece)
            if (e_row, e_col) in legal_moves:
                self.board[e_row][e_col] = piece
                piece.pos = (e_row, e_col)
                self.board[s_row][s_col] = 0
                self.white_to_move = not self.white_to_move
                if isinstance(piece, King):
                    if piece.color == 'w':
                        self.white_king_pos = (e_row, e_col)
                    else:
                        self.black_king_pos = (e_row, e_col)

    def get_piece(self, row, col):
        return self.board[row][col]

    def get_board(self):
        return self.board

    def is_under_attack(self, pos, enemy_color):
        for r in range(DIMENSION):
            for c in range(DIMENSION):
                piece = self.board[r][c]
                if piece != 0 and piece.color == enemy_color:
                    if isinstance(piece, Pawn):
                        attacks = piece.get_attack_moves(self.board)
                    else:
                        attacks = piece.get_valid_moves(self.board)
                    if pos in attacks:
                        return True
        return False

    def get_legal_moves(self, piece):
        legal_moves = []
        enemy_color = 'w' if piece.color == 'b' else 'b'
        moves = piece.get_valid_moves(self.board)
        start_row, start_col = piece.pos

        for move in moves:
            end_row, end_col = move
            target_piece = self.board[end_row][end_col]

            #we make a virtual move
            self.board[end_row][end_col] = piece
            self.board[start_row][start_col] = 0
            piece.pos = (end_row, end_col)
            if isinstance(piece, King):
                temp_king_pos = (end_row, end_col)
            else:
                temp_king_pos = self.white_king_pos if piece.color == 'w' else self.black_king_pos

            if not self.is_under_attack(temp_king_pos, enemy_color):
                legal_moves.append(move)
            self.board[end_row][end_col] = target_piece
            self.board[start_row][start_col] = piece
            piece.pos = (start_row, start_col)

        return legal_moves
