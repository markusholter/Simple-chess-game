let socket = io.connect("ws://127.0.0.1:5000")

socket.on("start", function(_) {
    document.getElementById("status").innerHTML = "Start!"
    socket.emit("getOpponent")
})

socket.on("opponent", function(opponent) {
    document.getElementById("opponent").innerHTML = opponent
})

socket.on("alert", function(text) {
    alert(text)
    window.location.href = "/"
})

// Old
document.getElementById("connect").onclick = function() {
    socket.emit("message", "Hello")
}