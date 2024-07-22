from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)

socket = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socket.on("connect")
def handle_connect():
    app.logger.info("Client connected")

@socket.on("message")
def handle_message(data):
    app.logger.info("The data: " + data)

@app.route("/send")
def send_new():
    socket.emit("message", "New hello world!")
    return "Success!"

if __name__ == "__main__":
    socket.run(app, debug=True)