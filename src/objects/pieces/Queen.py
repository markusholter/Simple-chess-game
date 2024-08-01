from ..pieces.Piece import Piece

class Queen(Piece):
    def __init__(self, white: bool, image: str) -> None:
        super().__init__(white, image)

    def turn(self, start, end, board):
        # Rule for checking if queen is moved in something else than a straight line/diagonal
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
    
    def canTake(self, white, vertical, horizontal, distance):
        if white == self.white: return False
        return True