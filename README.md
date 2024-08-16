## Prerequisites
- Python 3.10.12 or later
- Python venv package

## Pieces
Currently got pictures of chess pieces from this site:
https://greenchess.net/info.php?item=downloads

## Virtual environment
- Make one with venv:
```
$ mkdir myproject
$ cd myproject
$ python3 -m venv .venv
$ . .venv/bin/activate
```

- Install flask and flask-socketio:
```
pip install flask flask-socketio
```

### For testing
- Install pytest
```
pip install pytest
```

- Append path to src folder to the .venv.bin.activate file
- Run test with command 
```
pytest
```

## TODOs
- Fix row-numbers in style.css is adjusted with margin-bottom to account for screen name beneath chessboard.
- Fix reloading in game removes board and backend room
- Add functionality so pawn can attack other pawn if moved two spaces
- Add functionality so pawn can transform when reaching end of board
- Add tests for more than the piece.turn method
    - Maybe a whole test game?