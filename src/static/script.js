let socket = io.connect("ws://127.0.0.1:5000")
var currentParentId
var currentImage = null
var turn = null

socket.on("you", function() {
    if (turn == null || true) {
        turn = true
        document.getElementById("status").innerHTML = "Your turn"
        socket.emit("getOpponent")
    }
})

socket.on("opponent", function() {
    if (turn == null || true) {
        turn = false
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
    if (turn) {
        var move

        // Sends coordinates even if there is a picture at the place of drop
        if (event.target.id) move = currentParentId + "," + event.target.id
        else {
            var targetParent = event.target.closest(".cell")
            move = currentParentId + "," + targetParent.id
        }
        socket.emit("turn", move)    
    }
    

    return
    document.getElementById(currentParentId).innerHTML = ""
    event.target.appendChild(currentImage)
}