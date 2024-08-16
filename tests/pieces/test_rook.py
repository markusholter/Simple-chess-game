from objects.Board import Board
from objects.pieces.Rook import Rook

# Using GPT to generate test cases

def test_rook_horizontal_move():
    board = Board()
    # Place the rook at (4, 4) for a clear horizontal move
    board.get_white_board()[2][4][4] = ("cell white", Rook(True, "rook-w.svg"), "4 4")
    rook = board.get_white_board()[2][4][4][1]
    start = [4, 4]
    end = [4, 7]
    assert rook.turn(start, end, board.get_white_board()[2]), "Rook should move horizontally."

def test_rook_vertical_move():
    board = Board()
    # Place the rook at (4, 4) for a clear vertical move
    board.get_white_board()[2][4][4] = ("cell white", Rook(True, "rook-w.svg"), "4 4")
    rook = board.get_white_board()[2][4][4][1]
    start = [4, 4]
    end = [1, 4]
    assert rook.turn(start, end, board.get_white_board()[2]), "Rook should move vertically."

def test_rook_invalid_move_diagonally():
    board = Board()
    # Place the rook at (4, 4) to test invalid diagonal move
    board.get_white_board()[2][4][4] = ("cell white", Rook(True, "rook-w.svg"), "4 4")
    rook = board.get_white_board()[2][4][4][1]
    start = [4, 4]
    end = [2, 2]  # Invalid move for a rook (moving diagonally like a bishop)
    assert not rook.turn(start, end, board.get_white_board()[2]), "Rook should not move diagonally."

def test_rook_move_with_obstacle_in_path():
    board = Board()
    rook = board.get_white_board()[2][7][0][1]  # White rook at initial position (7, 0)
    start = [7, 0]
    end = [4, 0]
    # Pawns are already in the way from the initial board setup
    assert not rook.turn(start, end, board.get_white_board()[2]), "Rook should not move through other pieces."

def test_rook_move_backwards_vertically():
    board = Board()
    # Place the rook at (4, 4) for testing backward vertical movement
    board.get_white_board()[2][4][4] = ("cell white", Rook(True, "rook-w.svg"), "4 4")
    rook = board.get_white_board()[2][4][4][1]
    start = [4, 4]
    end = [6, 4]
    assert rook.turn(start, end, board.get_white_board()[2]), "Rook should be able to move backward vertically."

def test_rook_move_backwards_horizontally():
    board = Board()
    # Place the rook at (4, 4) for testing backward horizontal movement
    board.get_white_board()[2][4][4] = ("cell white", Rook(True, "rook-w.svg"), "4 4")
    rook = board.get_white_board()[2][4][4][1]
    start = [4, 4]
    end = [4, 2]
    assert rook.turn(start, end, board.get_white_board()[2]), "Rook should be able to move backward horizontally."
