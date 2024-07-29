from ..pieces.Piece import Piece

class Bishop(Piece):
    def __init__(self, white: bool, image: str) -> None:
        super().__init__(white, image)

    def turn(self, start, end, board):
        # Rule for checking that bishop is movin diagonally
        if abs(end[0] - start[0]) != abs(end[1] - start[1]):
            return False
        
        if start[0] < end[0]: vertical = 1
        else: vertical = -1

        if start[1] < end[1]: horizontal = 1
        else: horizontal = -1
        
        return self.checkObstacle(start, end, board, vertical, horizontal)