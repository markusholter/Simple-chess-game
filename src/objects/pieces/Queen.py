from ..pieces.Piece import Piece

class Queen(Piece):
    def __init__(self, white: bool, image: str) -> None:
        super().__init__(white, image)

    def turn(self, start, end, board):
        if (abs(end[0] - start[0]) != abs(end[1] - start[1]) and
                not (start[0] == end[0] and start[1] != end[1]) and
                not (start[0] != end[0] and start[1] == end[1])
                ):
            return False
        
        vertical = 0
        horizontal = 0        
        if start[0] < end[0]: vertical = 1
        elif start[0] > end[0]: vertical = -1

        if start[1] < end[1]: horizontal = 1
        elif start[1] > end[1]: horizontal = -1

        return self.checkObstacle(start, end, board, vertical, horizontal)