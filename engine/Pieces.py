class Piece:
    def __init__(self, color, pos):
        self.color = color
        self.pos = pos
        self.image_name = color + self.__class__.__name__[0]

class Pawn(Piece):
    pass

class Rook(Piece):
    pass

class Knight(Piece):
    def __init__(self, color, pos):
        super().__init__(color, pos)
        self.image_name = color + "N"

class Bishop(Piece):
    pass

class Queen(Piece):
    pass

class King(Piece):
    pass

