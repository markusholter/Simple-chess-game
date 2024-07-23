from flask import current_app, Blueprint, render_template, request, redirect, url_for, session, flash
from objects.Room import Room

bp = Blueprint("start", __name__)

@bp.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        error = None

        session.clear()

        username = request.form["username"]
        roomName = request.form["room"]

        session["userId"] = username
        session["roomName"] = roomName

        if username_exists(username):
            error = "That name is taken!"

        elif room_full(roomName):
            error = "That room is full!"

        if error is None:
            current_app.logger.info(f"Got username: {session.get('userId')} with room: {session.get('roomName')}")
            return redirect(url_for("start.loading"))
        
        flash(error)

    return render_template("start/index.html")

def username_exists(username: str):
    return username in current_app.config["USERNAMES"]

def room_full(roomName):
    rooms: dict[str, Room] = current_app.config["ROOMS"]

    if roomName not in rooms: return False
    return not rooms[roomName].getWaiting()

@bp.route("/loading")
def loading():
    return render_template("start/loading.html")