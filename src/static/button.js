let socket = io.connect("ws://127.0.0.1:5000")

document.getElementById("button").onclick = function() {
    socket.emit("message", "Hello")
}

socket.on("message", function(data)  {
    document.getElementById("world").innerHTML = data
}) 