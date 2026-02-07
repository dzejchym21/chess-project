# TODO:
#  implement abstract class Pieces
class Piece:
    def __init__(self, color, pos):
        self.color = color
        self.pos = pos
        self.image_name = color + self.__class__.__name__[0]

class Pawn(Piece):
    pass

