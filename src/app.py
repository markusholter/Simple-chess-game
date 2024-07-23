from flask import Flask, session, url_for
from flask_socketio import SocketIO, join_room, leave_room, emit

import start
import game
from objects.Room import Room

class Config:
    SECRET_KEY = "dev"
    USERNAMES: set[str] = set()
    ROOMS: dict[str, Room] = {}

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(start.bp)
app.register_blueprint(game.bp)

socket = SocketIO(app)

usernames: set[str] = app.config["USERNAMES"]
rooms: dict[str, Room] = app.config["ROOMS"]

@socket.on("connect")
def handle_connect(_):
    roomName = session.get("roomName")
    player = session.get("userId")

    usernames.add(session.get("userId"))

    if roomName not in rooms:
        app.logger.info("Creating room")
        room = Room(roomName, player)
        rooms[roomName] = room

        join_room(roomName)
        
    else:
        room: Room = rooms[roomName]
        if not room.getWaiting(): return

        app.logger.info("Adding Player2 to room")
        room.addPlayer2(player)
        join_room(roomName)
        emit("start", url_for("game.board"), to=roomName)
    

    app.logger.info(f"Client connected with userId {session.get('userId')}")

@socket.on("disconnect")
def handle_disconnect():
    usernames.remove(session.get("userId"))
    app.logger.info(f"Client {session.get('userId')} disconnected")

@socket.on("message")
def handle_message(data):
    app.logger.info(f"Got message from {session.get('userId')} containing {data}")
    
    

@app.route("/send")
def send_new():
    socket.emit("message", "New hello world!")
    return "Success!"

if __name__ == "__main__":
    socket.run(app, debug=True)