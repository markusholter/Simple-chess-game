from ..pieces.Piece import Piece

class Rook(Piece):
    def __init__(self, white: bool, image: str) -> None:
        super().__init__(white, image)
        self.castle = True

    def canCastle(self): return self.castle
    def removeCastle(self): self.castle = False

    def turn(self, start, end, board):

        # Rule for checking if rook was attempted to move diagonally
        if start[0] != end[0] and start[1] != end[1]:
            return False
        
        # Rule for checking if rook was not moved
        if start[0] == end[0] and start[1] == end[1]:
            return False
        
        vertical, horizontal = Piece.getVerticalHorizontal(start, end)

        if not self.checkObstacle(start, end, board, vertical, horizontal):
            return False
        
        self.removeCastle()
        return True
    
    def canTake(self, white, vertical, horizontal, distance):
        if white == self.white: return False
        if abs(vertical) == 1 and abs(horizontal) == 1: return False
        if vertical == 0 and horizontal == 0: return False
        return True