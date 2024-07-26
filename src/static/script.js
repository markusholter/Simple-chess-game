let socket = io.connect("ws://127.0.0.1:5000")
var currentParent
var currentImage = null

socket.on("start", function() {
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

function drag(event) {
    currentImage = event.target
    currentParent = currentImage.closest(".cell")
}

function allowDrop(event) {
    event.preventDefault()
}

function drop(event) {
    event.preventDefault()
    currentParent.innerHTML = ""
    event.target.appendChild(currentImage)
}

// Old
document.getElementById("connect").onclick = function() {
    socket.emit("message", "Hello")
}