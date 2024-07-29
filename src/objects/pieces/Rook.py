from ..pieces.Piece import Piece

class Rook(Piece):
    def __init__(self, white: bool, image: str) -> None:
        super().__init__(white, image)

    def turn(self, start, end, board):

        # Rule for checking if rook was attempted to move diagonally
        if start[0] != end[0] and start[1] != end[1]:
            return False
        
        # Rule for checking if rook was not moved
        if start[0] == end[0] and start[1] == end[1]:
            return False
        
        # Rule for checking color of possible attacked piece
        endpiece: Piece = board[end[0]][end[1]][1]
        if endpiece and endpiece.getWhite() == self.white:
            return False
        

        vertical = 0
        horizontal = 0
        if start[0] == end[0]:
            if start[1] < end[1]: horizontal = 1
            elif start[1] > end[1]: horizontal = -1
        
        if start[1] == end[1]:
            if start[0] < end[0]: vertical = 1
            elif start[0] > end[0]: vertical = -1

        return self.checkObstacle(start, end, board, vertical, horizontal)