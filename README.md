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

## Technical debt
- The row-numbers in style.css is adjusted with margin-bottom to account for screen name beneath chessboard.
- Reloading in game removes board and backend room

## Rules not implemented
- Castling
- Pawn can attack other pawn if moved two spaces
- Any representation check mate or stale mate
- Transformation of pawn when reaching end of board