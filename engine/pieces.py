class Piece:
    def __init__(self, color, pos):
        self.color = color
        self.pos = pos
        self.image_name = color + self.__class__.__name__[0]

    def get_valid_moves(self):
        pass

class Pawn(Piece):
    def get_valid_moves(self, board_array):
        moves = []
        r, c = self.pos
        direction = 1 if self.color == 'b' else -1

        if 0 <= r + direction < 8:
            if board_array[r + direction][c] == 0:
                moves.append((r + direction, c))

                start_row = 6 if self.color == 'w' else 1
                if r == start_row:
                    if board_array[r + 2 * direction][c] == 0:
                        moves.append((r + 2 * direction, c))

        for dc in [-1, 1]:
            new_row = r + direction
            new_col = c + dc
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                target_piece = board_array[new_row][new_col]
                if target_piece != 0 and target_piece.color != self.color:
                    moves.append((new_row, new_col))

        return moves


class Rook(Piece):
    pass

class Knight(Piece):
    def __init__(self, color, pos):
        super().__init__(color, pos)
        self.image_name = color + "N"

    def get_valid_moves(self, board_array):
        moves = []
        r, c = self.pos
        offsets = [
            (2, 1), (2,-1), (1,2), (1,-2),
            (-2, 1), (-2,-1), (-1,2), (-1,-2)
        ]

        for r_end, c_end in offsets:
            end_row = r + r_end
            end_col = c + c_end
            if 0 <= end_row < 8 and 0 <= end_col < 8:
                target_piece = board_array[end_row][end_col]
                if target_piece == 0 or target_piece.color != self.color:
                    moves.append((end_row, end_col))

        return moves


class Bishop(Piece):
    pass

class Queen(Piece):
    pass

class King(Piece):
    pass

