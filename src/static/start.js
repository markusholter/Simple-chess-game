let socket = io.connect("ws://127.0.0.1:5000")

socket.on("start", function(url) {
    window.location.href = url
})

// Old
document.getElementById("connect").onclick = function() {
    socket.emit("message", "Hello")
}