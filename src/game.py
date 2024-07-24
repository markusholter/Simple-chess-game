from flask import Blueprint, render_template, current_app, session
from objects.Board import Board
from objects.Room import Room

bp = Blueprint("game", __name__, url_prefix="/game")

@bp.route("/")
def board():
    username = session.get("userId")
    roomName = session.get("roomName")

    try:
        room: Room = current_app.config["ROOMS"][roomName]
        mainBoard: Board = room.getBoard()
        guiBoardData = mainBoard.get_white_board() if username == room.getPlayer1() else mainBoard.get_black_board()
    except:
        guiBoardData = [[], [], []]

    return render_template("game/board.html", rows=guiBoardData[0], cols=guiBoardData[1], board=guiBoardData[2])