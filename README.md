# Simple chess game
**Simple Chess Game** is a web application that allows users to play chess against each other online. Players can connect using a unique code and choose a screen name to identify themselves during gameplay.

This application is built with Python, utilizing Flask for handling HTTP requests and Flask-SocketIO for managing real-time game turns. The entire application is containerized with Docker, ensuring a smooth and consistent deployment on the server.

Not all chess rules are fully implemented yet, but future updates are planned to address them. The key rules still to be added include:
- Stalemate after threefold repetition
- En passant (capturing a pawn that moves two squares forward)
- Pawn promotion (transforming a pawn upon reaching the opponent's back rank)

## Try it out
You can try the Simple Chess Game by visiting the following ip-address:

[http://172.232.132.6](http://172.232.132.6)

## Features
- **Online chess game using connection code:** Play chess with friends online by sharing a unique connection code.
- **Real-time game updates via WebSockets:** Enjoy smooth, real-time gameplay with WebSocket technology.
- **Legal moves enforcement:** Backend logic ensures that only legal chess moves are allowed.
- **Dockerized for easy deployment:** Deploy the application easily on any platform with Docker.
- **Planned enhancements:** Upcoming features include stalemate detection, en passant moves, and pawn promotion.
- **Multiplayer support:** Connect and play with friends from anywhere over the internet.
- **Responsive design:** Enjoy seamless gameplay on any device with a responsive chessboard that adapts to different screen sizes.

## How to run production server through docker on localhost
1. Ensure docker is installed on your system
2. Verify that you have sufficient RAM/swap memory (8GB should suffice)
3. Navigate to the "Simple-chess-game" directory
4. Build docker image:
```
sudo docker build -t chess .
```
5. Run docker image:
```
sudo docker run -p 8000:80 -t chess
```
6. Open your browser and visit http://127.0.0.1:8000 to access the site.

## How to run development server
1. Ensure python3.10.12 or later is installed, along with python-venv.
2. Clone the repository
3. Create virtual environment with venv:
```
$ cd Simple-chess-game
$ python3 -m venv .venv
```

4. Modify the "activate" file inside ".venv/bin/" by adding the path to the "src" folder at the end:
``` 
export PYTHONPATH=/home/user/Simple-chess-game/src 
```

5. Initialize the virtual environment:
```
$ . .venv/bin/activate
```


6. Install the required python packages:
```
pip install flask flask-socketio pytest
```

7. Start development server:
```
flask run
```

8. Open your browser and visit http://127.0.0.1:5000 to access the site 

9. To run unit tests, execute the following:
```
pytest
```

## License and attribution
This project uses chess piece images from the Green Chess project. The images are provided under the [Creative Commons Attribution-ShareAlike License](https://creativecommons.org/licenses/by-sa/3.0/deed.en).

Some images are created by others and some by the Green Chess author. You are free to copy, redistribute, and modify these images as long as you attribute the original author and share any derived work under the same license.

- Chess Piece Images Source: [Green Chess](https://greenchess.net/info.php?item=downloads)
- License: [Creative Commons Attribution-ShareAlike 3.0 International License](https://creativecommons.org/licenses/by-sa/3.0/deed.en)