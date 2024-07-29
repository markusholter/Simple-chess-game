from ..pieces.Piece import Piece

class Pawn(Piece):
    def __init__(self, white: bool, image: str) -> None:
        super().__init__(white, image)

    def turn(self):
        return False