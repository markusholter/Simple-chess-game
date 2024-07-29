from ..pieces.Piece import Piece

class Knight(Piece):
    def __init__(self, white: bool, image: str) -> None:
        super().__init__(white, image)