from flask import current_app
from copy import deepcopy
from collections import defaultdict

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
        self.check = defaultdict(set)

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
    
    def turn(self, move: str, white: bool, fromUser=True):
        if fromUser: current_app.logger.info(f"Attempted move: {move}")
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
        
        # Make sure possible attacked piece is not of same colour and that the piece has not been dropped on its original place
        endpiece = self.board[end[0]][end[1]][1]
        if endpiece and white == endpiece.getWhite():
            return False
        
        # Make sure piece has been moved in relation to its moveset
        if not piece.turn(start, end, self.board):
            return False
        
        # Change position of kings saved in board so that it can be used in checkCheck()
        oldWhiteKing = self.whiteKing
        oldBlackKing = self.blackKing
        if isinstance(piece, King):
            if piece.getWhite(): self.whiteKing = tuple(end)
            else: self.blackKing = tuple(end)

        newBoard = self.makeNewBoard(start, end, piece)

        check = self.checkCheck(newBoard, log=fromUser)
        if fromUser: self.check = check

        # See if move attempted puts the player in check and reset boards saved positions if that is the case
        if check:
            if ((white and "w" in check) or
                    (not white and "b" in check) or
                    isinstance(piece, King)):
                
                self.whiteKing = oldWhiteKing
                self.blackKing = oldBlackKing
                return False
            
        # Reset boards saved position of kings if the function was not called from user
        if not fromUser and isinstance(piece, King):
            self.whiteKing = oldWhiteKing
            self.blackKing = oldBlackKing

        # Moves the piece in backend representation of board
        if fromUser: self.board = newBoard
        
        return [move]
    
    def makeNewBoard(self, start, end, piece):
        movedStart = (self.board[start[0]][start[1]][0], None, self.board[start[0]][start[1]][2])
        movedEnd = (self.board[end[0]][end[1]][0], piece, self.board[end[0]][end[1]][2])
        newBoard = deepcopy(self.board)
        newBoard[end[0]][end[1]] = movedEnd
        newBoard[start[0]][start[1]] = movedStart

        return newBoard

    
    def checkMateOrStale(self, white):
        if self.checkMate(white):
            return "mate"
        if self.checkStale(white):
            return "stale"
        return ""
    
    # Check if player is in stalemate
    def checkStale(self, white):
        if self.check: return False
        possibleMoves = [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1] if x != 0 and y != 0]
        possibleMoves.extend([(x, y) for x in [-2, -1, 1, 2] for y in [-2, -1, 1, 2] if abs(x + y) == 3])
        
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                for x, y in possibleMoves:
                    end = [i + x, j + y]
                    if end[0] < 0 or end[1] < 0 or end[0] >= len(self.board) or end[1] >= len(row):
                        continue

                    piece = cell[1]
                    if piece == None: continue
                    if self.turn(f"{i} {j},{end[0]} {end[1]}", white, False):
                        current_app.logger.info(f"{piece} Can move from {i} {j} to {end}")
                        return False 

        return True
    
    # Check if player is in checkmate
    def checkMate(self, white: bool):
        if not self.check: return False
        colour = "w" if white else "b"
        blockable = len(self.check[colour]) == 1
        if blockable:
            possibleBlocks = self.possibleBlocks(white, colour)
            current_app.logger.info(f"Possible blocks: {possibleBlocks}")

        # Go through board to try and move pieces
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                piece = cell[1]
                if not piece: continue
                if white != piece.getWhite(): continue

                # If piece is not king, check if piece can block
                if blockable and not isinstance(piece, King):
                    for pos in possibleBlocks:
                        if piece.turn([i, j], pos, self.board):
                            current_app.logger.info(f"{piece} at position {i, j} can block at position {pos}")
                            return False
                        
                # If piece is the king, try to move it and see if it still is in check
                if isinstance(piece, King):
                    possibleMoves = [[i + x, j + y] for x in [-1, 0, 1] for y in [-1, 0, 1] 
                                        if not (x == 0 and y == 0) and i + x >= 0 and j + y >= 0 and i + x < len(self.board) and j + y < len(row)]
                    for pos in possibleMoves:
                        if self.turn(f"{i} {j},{pos[0]} {pos[1]}", white, False):
                            current_app.logger.info(f"{piece} can move from position {i, j} to position {pos} to escape check")
                            return False

        return True
    
    # Get all cells in board a piece can move to to block the current check
    def possibleBlocks(self, white, colour):
        blocks = []
        start = next(iter(self.check[colour]))
        end = self.whiteKing if white else self.blackKing

        if isinstance(self.board[start[0]][start[1]][1], Knight):
            blocks.append(list(start))
            return blocks

        vertical, horizontal = Piece.getVerticalHorizontal(start, end)

        while start != end:
            blocks.append(list(start))
            start = (start[0] + vertical, start[1] + horizontal)

        return blocks
            
    # Check if any of the players are in check, and if so, the position of the piece attacking.
    def checkCheck(self, newBoard, log=True):
        check = defaultdict(set)

        # Go through all directions the king can be attacked from
        for vertical in [-1, 0, 1]:
            for horizontal in [-1, 0, 1]:
                if vertical == 0 and horizontal == 0: continue

                whiteCheck = self.checkKing(self.whiteKing, True, vertical, horizontal, newBoard, log)
                blackCheck = self.checkKing(self.blackKing, False, vertical, horizontal, newBoard, log)
                if whiteCheck: check["w"].add(whiteCheck)
                if blackCheck: check["b"].add(blackCheck)

        # Check knight outside of loop since it does not come from a specific direction
        whiteKnight = self.checkKnight(self.whiteKing, True, newBoard, log)
        blackKnight = self.checkKnight(self.blackKing, False, newBoard, log)
        if whiteKnight: check["w"].add(whiteKnight)
        if blackKnight: check["b"].add(blackKnight)

        return check
    
    # Check if specific king is attacked from specific direction. 
    def checkKing(self, king, white, vertical, horizontal, newBoard, log):
        row = king[0] + vertical
        col = king[1] + horizontal
        distance = 1

        while row < len(newBoard) and row >= 0 and col < len(newBoard[row]) and col >= 0:
            piece: Piece = newBoard[row][col][1]
            if not piece: 
                row += vertical
                col += horizontal
                distance += 1
                continue

            if piece.canTake(white, vertical, horizontal, distance): 
                if log: current_app.logger.info(f"Check by {type(piece)} detected from position {row} {col} to position {king}")
                return row, col
            return None
        
    # Individual check for if a knight is attacking King. Has to be done because it does not follow the same rules as the other pieces
    def checkKnight(self, king, white, newBoard, log):
        for vertical in [-2, -1, 1, 2]:
            for horizontal in [-2, -1, 1, 2]:
                if abs(vertical) + abs(horizontal) != 3: continue
               

                row = king[0] + vertical
                col = king[1] + horizontal
                if row >= len(newBoard) or row < 0: continue
                if col >= len(newBoard[row]) or col < 0: continue

                piece = newBoard[row][col][1]
                if isinstance(piece, Knight) and white != piece.getWhite():
                    if log: current_app.logger.info(f"Check by {type(piece)} detected from position {row} {col} to position {king}")
                    return row, col
        return None
                


if __name__ == "__main__":
    board = Board()
    for row in board.board:
        print(row)