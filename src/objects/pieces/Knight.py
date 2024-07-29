from ..pieces.Piece import Piece

class Knight(Piece):
    def __init__(self, white: bool, image: str) -> None:
        super().__init__(white, image)

    def turn(self, start, end, board):
        diffx = abs(end[0] - start[0])
        diffy = abs(end[1] - start[1])

        return diffx + diffy == 3