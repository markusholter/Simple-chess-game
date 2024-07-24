class Board:
    def __init__(self):
        self.board: list[list[tuple[str, str]]] = self.make_board()

    # Make board top to bottom from the white players perspective
    def make_board(self):
        return [
            [
                ("cell black", None) if (i + j) % 2 == 0 else ("cell white", None)
                for j in range(8)
            ]
            for i in range(8)
        ]
    
    def get_white_board(self):
        return self.board




if __name__ == "__main__":
    board = Board()
    for row in board.board:
        print(row)