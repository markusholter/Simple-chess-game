from . import Board

class Room:
    def __init__(self, roomName: str, player1: str, player2: str | None = None) -> None:
        self.roomName = roomName
        self.player1 = player1
        self.player2 = player2
        self.waiting = True
        self.turn = player1
        self.not_turn = player2
        self.board = Board.Board()

    def getRoomName(self): return self.roomName
    def getPlayer1(self): return self.player1
    def getPlayer2(self): return self.player2
    def getWaiting(self): return self.waiting
    def getBoard(self): return self.board
    def getTurn(self): return self.turn
    def getNotTurn(self): return self.not_turn

    def addPlayer2(self, player2):
        self.player2 = player2
        self.waiting = False
        self.not_turn = player2

    def switchTurn(self):
        curr = self.turn
        self.turn = self.not_turn
        self.not_turn = curr

    def checkTurn(self, move, username):
        return self.board.turn(move, True if username == self.player1 else False)