from objects.Board import Board
from objects.pieces.Queen import Queen

# Using GPT to generate test cases

def test_queen_horizontal_move():
    board = Board()
    # Place the queen at (4, 4) for a clear horizontal move
    board.get_white_board()[2][4][4] = ("cell white", Queen(True, "queen-w.svg"), "4 4")
    queen = board.get_white_board()[2][4][4][1]
    start = [4, 4]
    end = [4, 7]
    assert queen.turn(start, end, board.get_white_board()[2]), "Queen should move horizontally."

def test_queen_vertical_move():
    board = Board()
    # Place the queen at (4, 4) for a clear vertical move
    board.get_white_board()[2][4][4] = ("cell white", Queen(True, "queen-w.svg"), "4 4")
    queen = board.get_white_board()[2][4][4][1]
    start = [4, 4]
    end = [1, 4]
    assert queen.turn(start, end, board.get_white_board()[2]), "Queen should move vertically."

def test_queen_diagonal_move():
    board = Board()
    # Place the queen at (4, 4) for a clear diagonal move
    board.get_white_board()[2][4][4] = ("cell white", Queen(True, "queen-w.svg"), "4 4")
    queen = board.get_white_board()[2][4][4][1]
    start = [4, 4]
    end = [2, 2]
    assert queen.turn(start, end, board.get_white_board()[2]), "Queen should move diagonally."

def test_queen_invalid_move():
    board = Board()
    # Place the queen at (4, 4) to test invalid L-shape move (like a knight)
    board.get_white_board()[2][4][4] = ("cell white", Queen(True, "queen-w.svg"), "4 4")
    queen = board.get_white_board()[2][4][4][1]
    start = [4, 4]
    end = [6, 5]  # Invalid move for a queen (moving like a knight)
    assert not queen.turn(start, end, board.get_white_board()[2]), "Queen should not move like a knight."

def test_queen_move_with_obstacle_in_path():
    board = Board()
    queen = board.get_white_board()[2][7][3][1]  # White queen at initial position (7, 3)
    start = [7, 3]
    end = [4, 3]
    # Pawns are already in the way from the initial board setup
    assert not queen.turn(start, end, board.get_white_board()[2]), "Queen should not move through other pieces."

def test_queen_move_backwards_horizontally():
    board = Board()
    # Place the queen at (4, 4) for testing backward horizontal movement
    board.get_white_board()[2][4][4] = ("cell white", Queen(True, "queen-w.svg"), "4 4")
    queen = board.get_white_board()[2][4][4][1]
    start = [4, 4]
    end = [4, 2]
    assert queen.turn(start, end, board.get_white_board()[2]), "Queen should be able to move backward horizontally."

def test_queen_move_backwards_vertically():
    board = Board()
    # Place the queen at (4, 4) for testing backward vertical movement
    board.get_white_board()[2][4][4] = ("cell white", Queen(True, "queen-w.svg"), "4 4")
    queen = board.get_white_board()[2][4][4][1]
    start = [4, 4]
    end = [6, 4]
    assert queen.turn(start, end, board.get_white_board()[2]), "Queen should be able to move backward vertically."

def test_queen_move_backwards_diagonally():
    board = Board()
    # Place the queen at (4, 4) for testing backward diagonal movement
    board.get_white_board()[2][4][4] = ("cell white", Queen(True, "queen-w.svg"), "4 4")
    queen = board.get_white_board()[2][4][4][1]
    start = [4, 4]
    end = [6, 2]
    assert queen.turn(start, end, board.get_white_board()[2]), "Queen should be able to move backward diagonally."
