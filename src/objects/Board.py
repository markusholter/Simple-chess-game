from flask import current_app
from objects.pieces.Piece import Piece
from objects.pieces.Pawn import Pawn
from objects.pieces.King import King
from objects.pieces.Queen import Queen
from objects.pieces.Bishop import Bishop
from objects.pieces.Knight import Knight
from objects.pieces.Rook import Rook

class Board:
    def __init__(self):
        self.board: list[list[tuple[str, str]]] = self.make_board()
        self.rows: list[str] = [str(x) for x in range(8, 0, -1)]
        self.cols: list[str] = ["A", "B", "C", "D", "E", "F", "G", "H"]

    # Make board top to bottom from the white players perspective
    def make_board(self):
        piece_positions = {
    0: [
        Rook(False, "rook-b.svg"),
        Knight(False, "knight-b.svg"),
        Bishop(False, "bishop-b.svg"),
        Queen(False, "queen-b.svg"),
        King(False, "king-b.svg"),
        Bishop(False, "bishop-b.svg"),
        Knight(False, "knight-b.svg"),
        Rook(False, "rook-b.svg")
    ],
    1: [Pawn(False, "pawn-b.svg")] * 8,
    6: [Pawn(True, "pawn-w.svg")] * 8,
    7: [
        Rook(True, "rook-w.svg"),
        Knight(True, "knight-w.svg"),
        Bishop(True, "bishop-w.svg"),
        Queen(True, "queen-w.svg"),
        King(True, "king-w.svg"),
        Bishop(True, "bishop-w.svg"),
        Knight(True, "knight-w.svg"),
        Rook(True, "rook-w.svg")
    ]
}

        return [
            [
                ("cell black", piece_positions.get(i, [None] * 8)[j], f"{i} {j}") if (i + j) % 2 == 1 
                else ("cell white", piece_positions.get(i, [None] * 8)[j], f"{i} {j}")
                for j in range(8)
            ]
            for i in range(8)
        ]
    
    def get_white_board(self):
        return self.rows, self.cols, self.board
    
    def get_black_board(self):
        return self.rows[::-1], self.cols[::-1], [x[::-1] for x in self.board][::-1]
    
    def turn(self, move: str, white: bool):
        current_app.logger.info(f"Attempted move: {move}")

        start = [int(x) for x in move.split(",")[0].split(" ")]
        end = [int(x) for x in move.split(",")[1].split(" ")]
        
        piece: Piece = self.board[start[0]][start[1]][1]
        if white != piece.getWhite():
            return False
        
        if not piece.turn(start, end, self.board):
            return False

        self.board[end[0]][end[1]] = (self.board[end[0]][end[1]][0], piece, self.board[end[0]][end[1]][2])
        self.board[start[0]][start[1]] = (self.board[start[0]][start[1]][0], None, self.board[start[0]][start[1]][2])
        current_app.logger.info("Got there")
        return True



if __name__ == "__main__":
    board = Board()
    for row in board.board:
        print(row)