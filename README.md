## Pieces
Currently got pictures of chess pieces from this site:
https://greenchess.net/info.php?item=downloads

## How to run production server through docker on localhost
- Make sure docker is installed
- Make sure you are in "Simple-chess-game" directory
- Build docker image:
```
sudo docker build -t chess .
```
- Run docker image:
```
sudo docker run -p 8000:80 -t chess
```
- You can now visit 127.0.0.1:8000 in your browser to see the site.

## How to run development server
- Make sure python3.10.12 or later is installed, as well as python-venv.
- Clone repository
- Make virtual environment with venv:
```
$ cd Simple-chess-game
$ python3 -m venv .venv
```

- Add path src-folder at the end of the file "activate" inside .venv/bin/:
``` 
export PYTHONPATH=/home/user/Simple-chess-game/src 
```

- Initialize environment:
```
$ . .venv/bin/activate
```


- Install python packages:
```
pip install flask flask-socketio pytest
```

- Start development server:
```
flask run
```

- You can now visit 127.0.0.1:5000 in your browser to see the site. 

- To run unit tests, run pytest command:
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