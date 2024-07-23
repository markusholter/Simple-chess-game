let socket = io.connect("ws://127.0.0.1:5000")

socket.on("message", function(data) {
    document.getElementById("status").innerHTML = data
})

document.getElementById("connect").onclick = function() {
    socket.emit("message", "Hello")
}