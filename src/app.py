from flask import Flask, render_template, session
from flask_socketio import SocketIO

import start

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY="dev"
)

app.register_blueprint(start.bp)

socket = SocketIO(app)

usernames = set()

@socket.on("connect")
def handle_connect(auth):
    usernames.add(session.get("userId"))
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