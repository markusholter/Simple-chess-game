let socket = io.connect("ws://127.0.0.1:5000")

socket.on("start", function(player) {
    document.getElementById("status").innerHTML = "Start!"
    turn(player)
})

function turn(player) {

}

socket.on("alert", function(text) {
    alert(text)
    window.location.href = "/"
})

// Old
document.getElementById("connect").onclick = function() {
    socket.emit("message", "Hello")
}