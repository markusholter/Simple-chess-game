from flask import Blueprint, render_template
from objects.Board import Board

bp = Blueprint("game", __name__, url_prefix="/game")

@bp.route("/")
def board():
    board = Board()
    return render_template("game/board.html", board=board.get_white_board())