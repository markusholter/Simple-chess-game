let socket = io.connect("ws://127.0.0.1:5000")
var currentParentId
var currentImage = null
var turn = null

socket.on("you", function() {
    if (turn == null) {
        turn = true
        document.getElementById("status").innerHTML = "Your turn"
        socket.emit("getOpponent")
    }
})

socket.on("opponent", function() {
    if (turn == null) {
        document.getElementById("status").innerHTML = "Opponents turn"
        socket.emit("getOpponent")
    }
})

socket.on("opponentName", function(opponent) {
    document.getElementById("opponent").innerHTML = opponent
})

socket.on("alert", function(text) {
    alert(text)
    window.location.href = "/"
})

function drag(event) {
    currentImage = event.target
    currentParentId = currentImage.closest(".cell").id
}

function allowDrop(event) {
    event.preventDefault()
}

function drop(event) {
    event.preventDefault()
    document.getElementById(currentParentId).innerHTML = ""
    event.target.appendChild(currentImage)
}