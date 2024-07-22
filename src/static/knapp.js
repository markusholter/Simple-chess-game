let socket = io.connect("ws://127.0.0.1:5000")

document.getElementById("knapp").onclick = function() {
    socket.emit("message", "heii")
}