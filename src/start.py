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
            if create_room(username, roomName): 
                return redirect(url_for("game.board"))
            else:
                error = "Couldn't connect to room"
        
        flash(error)

    return render_template("start/index.html")

def create_room(player, roomName):
    usernames: set[str] = current_app.config["USERNAMES"]
    rooms: dict[str, Room] = current_app.config["ROOMS"]

    usernames.add(player)

    if roomName not in rooms:
        current_app.logger.info("Creating room-object")
        room = Room(roomName, player)
        rooms[roomName] = room

    else:
        room: Room = rooms[roomName]
        if not room.getWaiting(): return False

        current_app.logger.info("Adding Player2 to room-object")
        room.addPlayer2(player)

    return True

def username_exists(username: str):
    return username in current_app.config["USERNAMES"]

def room_full(roomName):
    rooms: dict[str, Room] = current_app.config["ROOMS"]

    if roomName not in rooms: return False
    return not rooms[roomName].getWaiting()