from ..pieces.Piece import Piece
from ..pieces.Rook import Rook

class King(Piece):
    def __init__(self, white: bool, image: str) -> None:
        super().__init__(white, image)
        self.castle = True

    def canCastle(self): return self.castle
    def removeCastle(self): self.castle = False

    def turn(self, start, end, board):

        distance = end[1] - start[1]
        if self.castle and abs(distance) == 2 and start[0] == end[0]:
            rookPosition = 0 if distance < 0 else len(board[0]) - 1
            rook = board[start[0]][rookPosition][1]
            if isinstance(rook, Rook) and rook.canCastle():
                return True

        # Rule to check if move was more than one to any side
        if abs(start[0] - end[0]) > 1 or abs(start[1] - end[1]) > 1:
            return False
        
        return True
    
    def canTake(self, white, vertical, horizontal, distance):
        if white == self.white: return False
        if distance > 1: return False
        return True