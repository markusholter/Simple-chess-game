class Piece:
    def __init__(self, white: bool, image: str) -> None:
        self.white = white
        self.image = image
    
    def getWhite(self): return self.white
    def getImage(self): return self.image

    def turn(self, start, end, board):
        return True
    
    """
    Checks if there are any pieces in the way of moving piece.
    Assumes that the move is possible with regards to direction and 
    that the only thing missing to determine if the move is legal
    is possibly blocking pieces.
    """
    def checkObstacle(self, start, end, board, vertical, horizontal):
        curr = start.copy()

        curr[0] += vertical
        curr[1] += horizontal

        while curr[0] != end[0] or curr[1] != end[1]:
            if board[curr[0]][curr[1]][1]:
                return False
            curr[0] += vertical
            curr[1] += horizontal

        return True