from objects.Board import Board
from objects.pieces.Bishop import Bishop
from objects.pieces.Pawn import Pawn

# Using GPT to generate test cases

def test_bishop_diagonal_move():
    board = Board()
    # Place the bishop at (4, 4) for a clear diagonal move
    board.get_white_board()[2][4][4] = ("cell white", Bishop(True, "bishop-w.svg"), "4 4")
    bishop = board.get_white_board()[2][4][4][1]
    start = [4, 4]
    end = [2, 2]
    assert bishop.turn(start, end, board.get_white_board()[2]), "Bishop should move diagonally."

def test_bishop_diagonal_move_other_direction():
    board = Board()
    # Place the bishop at (4, 4) for a clear diagonal move in the other direction
    board.get_white_board()[2][4][4] = ("cell white", Bishop(True, "bishop-w.svg"), "4 4")
    bishop = board.get_white_board()[2][4][4][1]
    start = [4, 4]
    end = [2, 6]
    assert bishop.turn(start, end, board.get_white_board()[2]), "Bishop should move diagonally in the other direction."

def test_bishop_invalid_move_straight_line():
    board = Board()
    # Place the bishop at (4, 4) to test invalid straight-line move
    board.get_white_board()[2][4][4] = ("cell white", Bishop(True, "bishop-w.svg"), "4 4")
    bishop = board.get_white_board()[2][4][4][1]
    start = [4, 4]
    end = [4, 6]  # Invalid move for a bishop (moving straight like a rook)
    assert not bishop.turn(start, end, board.get_white_board()[2]), "Bishop should not move in a straight line."

def test_bishop_move_with_obstacle_in_path():
    board = Board()
    bishop = board.get_white_board()[2][7][2][1]  # White bishop at initial position (7, 2)
    start = [7, 2]
    end = [5, 4]
    # Pawns are already in the way from the initial board setup
    assert not bishop.turn(start, end, board.get_white_board()[2]), "Bishop should not move through other pieces."

def test_bishop_move_backwards_diagonally():
    board = Board()
    # Place the bishop at (4, 4) for testing backward diagonal movement
    board.get_white_board()[2][4][4] = ("cell white", Bishop(True, "bishop-w.svg"), "4 4")
    bishop = board.get_white_board()[2][4][4][1]
    start = [4, 4]
    end = [6, 2]
    assert bishop.turn(start, end, board.get_white_board()[2]), "Bishop should be able to move backward diagonally."

def test_bishop_move_backwards_diagonally_other_direction():
    board = Board()
    # Place the bishop at (4, 2) for testing backward diagonal movement
    board.get_white_board()[2][4][2] = ("cell white", Bishop(True, "bishop-w.svg"), "4 2")
    bishop = board.get_white_board()[2][4][2][1]
    start = [4, 2]
    end = [6, 4]
    assert bishop.turn(start, end, board.get_white_board()[2]), "Bishop should be able to move backward diagonally in the other direction."
