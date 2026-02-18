from constaints import *
from engine.pieces import *

class Board:
    def __init__(self):
        self.board = [[0 for _ in range(DIMENSION)] for _ in range(DIMENSION)]
        self.white_to_move = True
        self.setup_board()
        self.black_king_pos = (0, 4)
        self.white_king_pos = (7, 4)
        self.en_passant_target = ()
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

                if isinstance(piece, King):
                    if abs(e_col - s_col) == 2:
                        if e_col == 6:
                            rook = self.board[s_row][7]
                            self.board[s_row][5] = rook
                            self.board[s_row][7] = 0
                            rook.pos = (s_row, 5)
                            rook.has_moved = True

                        elif e_col == 2:
                            rook = self.board[s_row][0]
                            self.board[s_row][3] = rook
                            self.board[s_row][0] = 0
                            rook.pos = (s_row, 3)
                            rook.has_moved = True

                    if piece.color == 'w':
                        self.white_king_pos = (e_row, e_col)
                    else:
                        self.black_king_pos = (e_row, e_col)

                if isinstance(piece, Pawn) and abs(e_row - s_row) == 2:
                    self.en_passant_target = ((e_row + s_row) // 2, e_col)
                elif isinstance(piece, Pawn) and (e_row, e_col) == self.en_passant_target:
                    self.board[s_row][e_col] = 0
                    self.en_passant_target = ()
                else:
                    self.en_passant_target = ()

                self.white_to_move = not self.white_to_move
                piece.has_moved = True
                print(self.en_passant_target)
                return True

        return False

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
                        attacks = piece.get_attack_moves()
                    else:
                        attacks = piece.get_valid_moves(self.board)
                    if pos in attacks:
                        return True
        return False

    def get_legal_moves(self, piece):
        legal_moves = []
        enemy_color = 'w' if piece.color == 'b' else 'b'
        if isinstance(piece, Pawn):
            moves = piece.get_valid_moves(self.board, self.en_passant_target)
        else:
            moves = piece.get_valid_moves(self.board)
        start_row, start_col = piece.pos

        if isinstance(piece, King):
            castle_moves = self.get_castling_moves(piece)
            legal_moves.extend(castle_moves)

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

    def check_end_game(self):
        current_color = 'w' if self.white_to_move else 'b'
        enemy_color = 'b' if self.white_to_move else 'w'

        for r in range(DIMENSION):
            for c in range(DIMENSION):
                piece = self.board[r][c]
                if piece != 0 and piece.color == current_color:
                    if len(self.get_legal_moves(piece)) > 0:
                        return None

        king_pos = self.white_king_pos if current_color == 'w' else self.black_king_pos
        if self.is_under_attack(king_pos, enemy_color):
            return "checkmate"
        else:
            return "stalemate"

    def is_clear(self, pos):
        row, col = pos
        return self.board[row][col] == 0

    def get_castling_moves(self, piece: 'King') -> list:
        moves = []
        if piece.has_moved:
            return moves
        enemy_color = 'w' if piece.color == 'b' else 'b'
        king_pos = piece.pos
        row = king_pos[0]
        piece1 = self.board[row][0]
        piece2 = self.board[row][7]
        if isinstance(piece1, Rook) and not piece1.has_moved:
            if all(self.is_clear((row, c)) for c in [1, 2, 3]):
                if all(not self.is_under_attack((row, col), enemy_color) for col in [2, 3, 4]):
                    moves.append((row, 2))

        if isinstance(piece2, Rook) and not piece2.has_moved:
            if all(self.is_clear((row, c)) for c in [5, 6]):
                if all(not self.is_under_attack((row, col), enemy_color) for col in [4, 5, 6]):
                    moves.append((row, 6))
        return moves

