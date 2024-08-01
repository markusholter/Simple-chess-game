from flask import current_app
from copy import deepcopy

from objects.pieces.Piece import Piece
from objects.pieces.Pawn import Pawn
from objects.pieces.King import King
from objects.pieces.Queen import Queen
from objects.pieces.Bishop import Bishop
from objects.pieces.Knight import Knight
from objects.pieces.Rook import Rook

class Board:
    def __init__(self):
        self.board: list[list[tuple[str, Piece, str]]] = self.make_board()
        self.rows: list[str] = [str(x) for x in range(8, 0, -1)]
        self.cols: list[str] = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.whiteKing = (7, 4)
        self.blackKing = (0, 4)
        self.check: str = ""

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
        current_app.logger.info(f"White kings position: {self.whiteKing}, black kings position: {self.blackKing}")
        """
        "Move" is a string in this format: "i j,i j"
        "i" is the row of the cell, and "j" is the col of the cell.
        A move has been attempted from "i j" in front of the comma to "i j" after the comma. 
        """

        start = [int(x) for x in move.split(",")[0].split(" ")]
        end = [int(x) for x in move.split(",")[1].split(" ")]
        
        piece = self.board[start[0]][start[1]][1]

        # Make sure user cannot move opponents piece
        if white != piece.getWhite():
            return False
        
        # Make sure possible attacked piece is not of same colour
        endpiece = self.board[end[0]][end[1]][1]
        if endpiece and white == endpiece.getWhite():
            return False
        
        # Make sure piece has been moved in relation to its moveset
        if not piece.turn(start, end, self.board):
            return False
        
        if isinstance(piece, King):
            if piece.getWhite(): self.whiteKing = tuple(end)
            else: self.blackKing = tuple(end)

        
        movedStart = (self.board[start[0]][start[1]][0], None, self.board[start[0]][start[1]][2])
        movedEnd = (self.board[end[0]][end[1]][0], piece, self.board[end[0]][end[1]][2])
        newBoard = deepcopy(self.board)
        newBoard[end[0]][end[1]] = movedEnd
        newBoard[start[0]][start[1]] = movedStart


        check = self.checkCheck(newBoard)
        if check:
            if white and check == "w": return False
            if not white and check == "b": return False

        # Moves the piece in backend representation of board
        self.board[end[0]][end[1]] = movedEnd
        self.board[start[0]][start[1]] = movedStart
        
        return True

    def checkCheck(self, newBoard):
        for vertical in [-1, 0, 1]:
            for horizontal in [-1, 0, 1]:
                if vertical == 0 and horizontal == 0: continue
                if self.checkKing(self.whiteKing, True, vertical, horizontal, newBoard): return "w"
                if self.checkKing(self.blackKing, False, vertical, horizontal, newBoard): return "b"

        return ""
    
    def checkKing(self, king, white, vertical, horizontal, newBoard):
        row = king[0] + vertical
        col = king[1] + horizontal
        distance = 1

        while row < len(newBoard) and col < len(newBoard[row]):
            piece: Piece = newBoard[row][col][1]
            if not piece: 
                row += vertical
                col += horizontal
                distance += 1
                continue

            if piece.canTake(white, vertical, horizontal, distance): return True
            return False


if __name__ == "__main__":
    board = Board()
    for row in board.board:
        print(row)