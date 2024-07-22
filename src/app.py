from flask import Flask, render_template, session
from flask_socketio import SocketIO, join_room, leave_room, emit

import start
from objects.Room import Room

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY="dev"
)

app.register_blueprint(start.bp)

socket = SocketIO(app)

usernames = set() 
rooms = {}

@socket.on("connect")
def handle_connect(_):
    usernames.add(session.get("userId"))
    app.logger.info(f"Client connected with userId {session.get('userId')}")

@socket.on("disconnect")
def handle_disconnect():
    usernames.remove(session.get("userId"))
    app.logger.info(f"Client {session.get('userId')} disconnected")

@socket.on("message")
def handle_message(data):
    app.logger.info(f"Got message from {session.get('userId')} containing {data}")

@socket.on("join")
def on_join(_):
    roomName = session.get("room")
    player = session.get("userId")

    if roomName not in rooms:
        room = Room(roomName, player)
        rooms[session.get("room")] = room

        join_room(roomName)
        return
    
    room: Room = rooms[roomName]
    if room.getWaiting():
        app.logger.info("Adding Player2")
        room.addPlayer2(player)
        join_room(roomName)
        emit("message", "Ready to start", to=roomName)
        return
    
    

@app.route("/send")
def send_new():
    socket.emit("message", "New hello world!")
    return "Success!"

if __name__ == "__main__":
    socket.run(app, debug=True)