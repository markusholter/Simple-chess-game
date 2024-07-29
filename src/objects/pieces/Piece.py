class Piece:
    def __init__(self, white: bool, image: str) -> None:
        self.white = white
        self.image = image
    
    def getWhite(self): return self.white
    def getImage(self): return self.image

    def turn(self):
        return True