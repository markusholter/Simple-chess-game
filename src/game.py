from flask import Blueprint, render_template
from objects.Board import Board

bp = Blueprint("game", __name__, url_prefix="/game")

@bp.route("/")
def board():
    mainBoard = Board()
    board = mainBoard.get_white_board()
    return render_template("game/board.html", rows=board[0], cols=board[1], board=board[2])