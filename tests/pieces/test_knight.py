from objects.Board import Board
from objects.pieces.Pawn import Pawn
from objects.pieces.Knight import Knight

# Using GPT to generate test cases

def test_knight_L_shape_move_forward():
    board = Board()
    knight = board.get_white_board()[2][7][1][1]  # White knight at initial position (7, 1)
    start = [7, 1]
    end = [5, 2]
    assert knight.turn(start, end, board.get_white_board()[2]), "Knight should move in an L-shape (2 forward, 1 sideways)."

def test_knight_L_shape_move_sideways():
    board = Board()
    knight = board.get_white_board()[2][7][1][1]  # White knight at initial position (7, 1)
    start = [7, 1]
    end = [5, 0]
    assert knight.turn(start, end, board.get_white_board()[2]), "Knight should move in an L-shape (2 forward, 1 sideways) in the other direction."

def test_knight_jump_over_pieces():
    board = Board()
    knight = board.get_white_board()[2][7][1][1]  # White knight at initial position (7, 1)
    start = [7, 1]
    end = [5, 2]
    # Simulate pawns blocking the path, but knight should be able to jump over them
    board.get_white_board()[2][6][0] = ("cell black", Pawn(True, "pawn-w.svg"), "6 0")
    board.get_white_board()[2][6][2] = ("cell black", Pawn(True, "pawn-w.svg"), "6 2")
    assert knight.turn(start, end, board.get_white_board()[2]), "Knight should be able to jump over other pieces."

def test_knight_invalid_move():
    board = Board()
    knight = board.get_white_board()[2][7][1][1]  # White knight at initial position (7, 1)
    start = [7, 1]
    end = [6, 1]  # Invalid move for a knight (moving straight like a rook/pawn)
    assert not knight.turn(start, end, board.get_white_board()[2]), "Knight should not move like a rook or a pawn."

def test_knight_move_backwards_L_shape():
    board = Board()
    # Place the knight at (5, 2) for testing backward movement
    board.get_white_board()[2][5][2] = ("cell black", Knight(True, "knight-w.svg"), "5 2")
    knight = board.get_white_board()[2][5][2][1]
    start = [5, 2]
    end = [7, 1]
    assert knight.turn(start, end, board.get_white_board()[2]), "Knight should be able to move backwards in an L-shape."

def test_knight_move_backwards_other_direction():
    board = Board()
    # Place the knight at (5, 0) for testing backward movement
    board.get_white_board()[2][5][0] = ("cell black", Knight(True, "knight-w.svg"), "5 0")
    knight = board.get_white_board()[2][5][0][1]
    start = [5, 0]
    end = [7, 1]
    assert knight.turn(start, end, board.get_white_board()[2]), "Knight should be able to move backwards in an L-shape in the other direction."
