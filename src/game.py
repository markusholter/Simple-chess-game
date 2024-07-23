from flask import Blueprint, render_template

bp = Blueprint("game", __name__, url_prefix="/game")

@bp.route("/")
def board():
    return render_template("game/board.html")