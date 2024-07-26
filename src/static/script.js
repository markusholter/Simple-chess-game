let socket = io.connect("ws://127.0.0.1:5000")
var currentParentId
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