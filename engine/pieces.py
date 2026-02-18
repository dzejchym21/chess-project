class Piece:
    def __init__(self, color, pos):
        self.color = color
        self.pos = pos
        self.image_name = color + self.__class__.__name__[0]
        self.has_moved = False

    def get_valid_moves(self, board_array):
        pass

    def get_sliding_moves(self, directions, board_array):
        moves = []
        r, c = self.pos
        for r_end, c_end in directions:
            for i in range(1,8):
                end_row = r + i * r_end
                end_col = c + i * c_end
                if 0 <= end_row < 8 and 0 <= end_col < 8:
                    target_piece = board_array[end_row][end_col]
                    if target_piece == 0:
                        moves.append((end_row, end_col))
                    elif target_piece != 0 and target_piece.color != self.color:
                        moves.append((end_row, end_col))
                        break
                    else:
                        break
                else:
                    break
        return moves

class Pawn(Piece):
    def get_valid_moves(self, board_array, ep_target):
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
                elif (new_row, new_col) == ep_target:
                    moves.append((new_row, new_col))

        return moves

    def get_attack_moves(self):
        moves = []
        row, col = self.pos
        direction = 1 if self.color == 'b' else -1

        for dc in [-1, 1]:
            new_row = row + direction
            new_col = col + dc
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                moves.append((new_row, new_col))

        return moves



class Rook(Piece):
    def get_valid_moves(self, board_array):
        offsets = [
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]
        return self.get_sliding_moves(offsets, board_array)


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
    def get_valid_moves(self, board_array):
        offsets = [
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        return self.get_sliding_moves(offsets, board_array)

class Queen(Piece):
    def get_valid_moves(self, board_array):
        offsets = [
            (1, 1), (1, -1), (-1, 1), (-1, -1),
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]
        return self.get_sliding_moves(offsets, board_array)

class King(Piece):
    def get_valid_moves(self, board_array):
        moves = []
        offsets= [
            (1, 1), (1, -1), (-1, 1), (-1, -1),
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]
        r, c = self.pos
        for r_end, c_end in offsets:
            new_row = r + r_end
            new_col = c + c_end
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                piece = board_array[new_row][new_col]
                if piece == 0:
                    moves.append((new_row, new_col))
                elif piece.color != self.color:
                    moves.append((new_row, new_col))
                else:
                    pass
        return moves
