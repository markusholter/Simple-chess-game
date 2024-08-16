from objects.Board import Board
from objects.pieces.King import King

# Using GPT to generate test cases

def test_king_horizontal_move():
    board = Board()
    # Place the king at (4, 4) for a one-square horizontal move
    board.get_white_board()[2][4][4] = ("cell white", King(True, "king-w.svg"), "4 4")
    king = board.get_white_board()[2][4][4][1]
    start = [4, 4]
    end = [4, 5]
    assert king.turn(start, end, board.get_white_board()[2]), "King should move one square horizontally."

def test_king_vertical_move():
    board = Board()
    # Place the king at (4, 4) for a one-square vertical move
    board.get_white_board()[2][4][4] = ("cell white", King(True, "king-w.svg"), "4 4")
    king = board.get_white_board()[2][4][4][1]
    start = [4, 4]
    end = [3, 4]
    assert king.turn(start, end, board.get_white_board()[2]), "King should move one square vertically."

def test_king_diagonal_move():
    board = Board()
    # Place the king at (4, 4) for a one-square diagonal move
    board.get_white_board()[2][4][4] = ("cell white", King(True, "king-w.svg"), "4 4")
    king = board.get_white_board()[2][4][4][1]
    start = [4, 4]
    end = [3, 3]
    assert king.turn(start, end, board.get_white_board()[2]), "King should move one square diagonally."

def test_king_invalid_move():
    board = Board()
    # Place the king at (4, 4) to test an invalid two-square move
    board.get_white_board()[2][4][4] = ("cell white", King(True, "king-w.svg"), "4 4")
    king = board.get_white_board()[2][4][4][1]
    start = [4, 4]
    end = [4, 6]  # Invalid move for a king (moving more than one square)
    assert not king.turn(start, end, board.get_white_board()[2]), "King should not move more than one square."

def test_king_move_backwards_horizontally():
    board = Board()
    # Place the king at (4, 4) for testing one-square backward horizontal movement
    board.get_white_board()[2][4][4] = ("cell white", King(True, "king-w.svg"), "4 4")
    king = board.get_white_board()[2][4][4][1]
    start = [4, 4]
    end = [4, 3]
    assert king.turn(start, end, board.get_white_board()[2]), "King should be able to move one square backward horizontally."

def test_king_move_backwards_vertically():
    board = Board()
    # Place the king at (4, 4) for testing one-square backward vertical movement
    board.get_white_board()[2][4][4] = ("cell white", King(True, "king-w.svg"), "4 4")
    king = board.get_white_board()[2][4][4][1]
    start = [4, 4]
    end = [5, 4]
    assert king.turn(start, end, board.get_white_board()[2]), "King should be able to move one square backward vertically."

def test_king_move_backwards_diagonally():
    board = Board()
    # Place the king at (4, 4) for testing one-square backward diagonal movement
    board.get_white_board()[2][4][4] = ("cell white", King(True, "king-w.svg"), "4 4")
    king = board.get_white_board()[2][4][4][1]
    start = [4, 4]
    end = [5, 5]
    assert king.turn(start, end, board.get_white_board()[2]), "King should be able to move one square backward diagonally."
