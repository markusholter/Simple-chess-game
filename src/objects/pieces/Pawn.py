from ..pieces.Piece import Piece

class Pawn(Piece):
    def __init__(self, white: bool, image: str) -> None:
        super().__init__(white, image)
        self.direction = -1 if self.white else 1
        self.doubleMove = False
        self.enpassant = False

    def removeDoubleMove(self): self.doubleMove = False
    def getEnpassant(self): return self.enpassant
    def removeEnpassent(self): self.enpassent = False

    def turn(self, start, end, board):
        endpiece: Piece | None = board[end[0]][end[1]][1]
        
        # Rules for moving pawn forward
        if (start[1] == end[1] and
                (end[0] - start[0]) * self.direction <= self.getDistance(start) and
                (end[0] - start[0]) * self.direction > 0 and
                not endpiece and
                self.checkObstacle(start, end, board, self.direction, 0)
                ):
            self.doubleMove = abs(start[0] - end[0]) == 2
            return True
        
        # Rules for using pawn to attack other pieces
        elif ((start[1] == end[1] + 1 or
                start[1] == end[1] - 1) and
                (end[0] - start[0]) * self.direction <= 1 and
                (end[0] - start[0]) * self.direction > 0 and
                (endpiece or self.checkEnemyDoubleMove(start, end, board))
                ):
            if self.checkEnemyDoubleMove(start, end, board): self.enpassant = True
            return True

        return False
    
    
    def checkEnemyDoubleMove(self, start, end, board):
        otherPiece = board[start[0]][end[1]][1]
        if isinstance(otherPiece, Pawn) and otherPiece.doubleMove: return True
        return False

    
    def canTake(self, white, vertical, horizontal, distance):
        if white == self.white: return False
        if distance > 1: return False
        if vertical == 0: return False
        if vertical == self.direction: return False
        if horizontal == 0: return False
        return True
    
    def getDistance(self, start):
        origin = 6 if self.white else 1

        if start[0] == origin: return 2
        else: return 1