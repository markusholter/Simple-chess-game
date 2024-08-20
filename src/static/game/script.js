let socket = io()
var currentParentId
var turn = null

socket.on("you", function(move) {
    doTurn(true, move)
})

socket.on("opponent", function(move) {
    doTurn(false, move)
})

function doTurn(mine, move) {
    if (turn == null) {
        socket.emit("getOpponent")
    }
    turn = mine
    document.getElementById("status").innerHTML = (turn) ? "Your turn" : "Opponents turn"
    if (!move) return

    if (move.includes("enpassant")) {
        start = move.split(",")[1]
        end = move.split(",")[2]
        removeAttackedPassant(start, end)
    } else {
        start = move.split(",")[0]
        end = move.split(",")[1]
    }

    var currentImage = document.getElementById(start).querySelector("img")
    var attackedImage = document.getElementById(end).querySelector("img")

    document.getElementById(start).removeChild(currentImage)
    if (attackedImage != null) document.getElementById(end).removeChild(attackedImage)
    document.getElementById(end).appendChild(currentImage)
}

socket.on("opponentName", function(opponent) {
    document.getElementById("opponent").innerHTML = opponent
})

socket.on("alert", function(text) {
    alert(text)
    window.location.href = "/"
})

function removeAttackedPassant(start, end) {
    var y = start.split(" ")[0]
    var x = end.split(" ")[1]
    var pos = y + " " + x
    attackedImage = document.getElementById(pos).querySelector("img")
    document.getElementById(pos).removeChild(attackedImage)
}

function drag(event) {
    var currentImage = event.target
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
    
}