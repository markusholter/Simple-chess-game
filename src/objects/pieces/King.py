from ..pieces.Piece import Piece

class King(Piece):
    def __init__(self, white: bool, image: str) -> None:
        super().__init__(white, image)

    def turn(self, start, end, board):
        # Rule to check if move was more than one to any side
        if abs(start[0] - end[0]) > 1 or abs(start[1] - end[1]) > 1:
            return False
        return True