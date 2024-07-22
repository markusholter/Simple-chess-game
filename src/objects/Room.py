class Room:
    def __init__(self, roomName: str, player1: str, player2: str | None = None) -> None:
        self.roomName = roomName
        self.player1 = player1
        self.player2 = player2
        self.waiting = True

    def getRoomName(self): return self.roomName
    def getPlayer1(self): return self.player1
    def getPlayer2(self): return self.player2
    def getWaiting(self): return self.waiting

    def addPlayer2(self, player2):
        self.player2 = player2
        self.waiting = False