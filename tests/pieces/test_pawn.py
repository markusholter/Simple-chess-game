import pytest

from objects.Board import Board
from objects.pieces.Pawn import Pawn

import pytest

# Using GPT to generate test cases

@pytest.fixture
def setup_board():
    return Board()

def test_pawn_one_square_forward(setup_board):
    board = setup_board
    pawn = board.get_white_board()[2][6][0][1]  # White pawn at initial position (6, 0)
    start = [6, 0]
    end = [5, 0]
    assert pawn.turn(start, end, board.get_white_board()[2]), "Pawn should move forward one square."

def test_pawn_two_squares_forward_first_move(setup_board):
    board = setup_board
    pawn = board.get_white_board()[2][6][0][1]  # White pawn at initial position (6, 0)
    start = [6, 0]
    end = [4, 0]
    assert pawn.turn(start, end, board.get_white_board()[2]), "Pawn should move forward two squares on first move."

def test_pawn_two_squares_forward_after_first_move(setup_board):
    board = setup_board
    pawn = board.get_white_board()[2][6][0][1]  # White pawn at initial position (6, 0)
    # First move one square forward
    assert pawn.turn([6, 0], [5, 0], board.get_white_board()[2])
    # Now try to move two squares forward
    start = [5, 0]
    end = [3, 0]
    assert not pawn.turn(start, end, board.get_white_board()[2]), "Pawn should not be able to move two squares after the first move."

def test_pawn_move_with_obstacle_in_front(setup_board):
    board = setup_board
    # Place an obstacle (another pawn) in front of the white pawn
    board.get_white_board()[2][5][0] = ("cell white", Pawn(True, "pawn-w.svg"), "5 0")  # White pawn as obstacle
    pawn = board.get_white_board()[2][6][0][1]  # White pawn at initial position (6, 0)
    start = [6, 0]
    end = [5, 0]
    assert not pawn.turn(start, end, board.get_white_board()[2]), "Pawn should not move forward with an obstacle in front."

def test_pawn_attempt_to_capture_forward(setup_board):
    board = setup_board
    # Place an enemy piece directly in front of the white pawn
    board.get_white_board()[2][5][0] = ("cell white", Pawn(False, "pawn-b.svg"), "5 0")  # Black pawn as enemy
    pawn = board.get_white_board()[2][6][0][1]  # White pawn at initial position (6, 0)
    start = [6, 0]
    end = [5, 0]
    assert not pawn.turn(start, end, board.get_white_board()[2]), "Pawn should not be able to capture by moving forward."

def test_pawn_capture_diagonally(setup_board):
    board = setup_board
    # Place an enemy piece diagonally in front of the white pawn
    board.get_white_board()[2][5][1] = ("cell black", Pawn(False, "pawn-b.svg"), "5 1")  # Black pawn as enemy
    pawn = board.get_white_board()[2][6][0][1]  # White pawn at initial position (6, 0)
    start = [6, 0]
    end = [5, 1]
    assert pawn.turn(start, end, board.get_white_board()[2]), "Pawn should be able to capture diagonally."

def test_pawn_attempt_to_move_diagonally_without_enemy(setup_board):
    board = setup_board
    pawn = board.get_white_board()[2][6][0][1]  # White pawn at initial position (6, 0)
    start = [6, 0]
    end = [5, 1]
    assert not pawn.turn(start, end, board.get_white_board()[2]), "Pawn should not move diagonally without an enemy piece."
