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