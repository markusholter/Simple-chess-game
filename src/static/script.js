let socket = io.connect("ws://127.0.0.1:5000")

socket.on("redirect", function(url) {
    window.location.href = url
})

socket.on("alert", function(text) {
    alert(text)
    window.location.href = "/"
})

// Old
document.getElementById("connect").onclick = function() {
    socket.emit("message", "Hello")
}