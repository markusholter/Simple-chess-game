from ..pieces.Piece import Piece

class Bishop(Piece):
    def __init__(self, white: bool, image: str) -> None:
        super().__init__(white, image)

    def turn(self, start, end, board):
        # Rule for checking that bishop is moving diagonally
        if abs(end[0] - start[0]) != abs(end[1] - start[1]):
            return False
        
        vertical, horizontal = Piece.getVerticalHorizontal(start, end)
        
        return self.checkObstacle(start, end, board, vertical, horizontal)
    
    def canTake(self, white, vertical, horizontal, distance):
        if white == self.white: return False
        if vertical == 0: return False
        if horizontal == 0: return False
        return True