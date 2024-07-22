from flask import Flask, render_template, session
from flask_socketio import SocketIO
from random import randint

import start

app = Flask(__name__)
app.register_blueprint(start.bp)

socket = SocketIO(app)

ids = []

@socket.on("connect")
def handle_connect():
    session.clear()
    
    userId = ids[-1] + 1 if len(ids) > 0 else 0
    ids.append(userId)
    session["userId"] = userId

    app.logger.info(f"Client connected with userId {userId}")

@socket.on("disconnect")
def handle_disconnect():
    ids.remove(session["userId"])
    app.logger.info(f"Client {session['userId']} disconnected")

@socket.on("message")
def handle_message(data):
    app.logger.info(f"Got message from {session['userId']} containing {data}")

@app.route("/send")
def send_new():
    socket.emit("message", "New hello world!")
    return "Success!"

if __name__ == "__main__":
    socket.run(app, debug=True)