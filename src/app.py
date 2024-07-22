from flask import Flask, render_template, session
from flask_socketio import SocketIO
from random import randint

app = Flask(__name__)

socket = SocketIO(app)

ids = [0]

@app.route("/")
def index():
    return render_template("index.html")

@socket.on("connect")
def handle_connect():
    session.clear()
    
    userId = ids[-1] + 1
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