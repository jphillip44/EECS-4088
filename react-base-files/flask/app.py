#!/usr/bin/python3
try:
    from eventlet import monkey_patch
    monkey_patch()
    print("Running Eventlet Server")
except ModuleNotFoundError:
    try:
        from gevent import monkey
        monkey.patch_all()
        print("Running Gevent Server")
    except ModuleNotFoundError:
        print("Running Flask Server")

import threading
import flask
import flask_socketio as sio

import desktop
from game_list import GameList
from display_game import DisplayGame

# initialize Flask

APP = flask.Flask(__name__)
SOCKETIO = sio.SocketIO(APP)

USERS = {}
GAME = None
THREAD = None
DISPLAY = DisplayGame()
# DISPLAY = None

# This is a catch-all route, this allow for react to do client-side
# routing and stoping flasks routing
@APP.route('/', defaults={'path': ''})
@APP.route('/<path:path>')
def index(path):
    return flask.render_template('index.html')

@SOCKETIO.on('joinServer')
def join_server(data):
    "Create a game lobby"
    USERS[data["socketId"]] = data["username"] + " #" + data["socketId"][:4]
    print(USERS.get(data["socketId"])  + " has logged in")
    sio.emit('games', {'games': GameList.list_games()})
    sio.emit('username', {'username': USERS[data["socketId"]]})
    sio.join_room(USERS[data["socketId"]])
    global GAME
    display()
    global DISPLAY
    # if DISPLAY is None:
    #     DISPLAY = DisplayGame()
    if DISPLAY is not None and (GAME is None or not GAME.active):
        DISPLAY.update(list(USERS.values()))

@SOCKETIO.on('createGame')
def create_game(data):
    global GAME
    print(USERS)
    if GAME is None or not GAME.active:
        GAME = GameList.select_game(data, list(USERS.values()), \
            socketio=SOCKETIO, display_game=DISPLAY)
        sio.emit('gameStarted', GAME.__name__, broadcast=True)
        global THREAD
        if THREAD is None or not THREAD.isAlive():
            THREAD = threading.Thread(target=GAME.run_game)
            THREAD.start()
            threading.Thread(target=check_thread).start()
        
def check_thread():
    THREAD.join()
    DISPLAY.update(list(USERS.values()))

def display():
    print("users")
    if USERS:
        print(*USERS.values(), sep='\n')
    else:
        print('none')

# When the client disconnects from the socket
@SOCKETIO.on('disconnect')
def disconnect():
    if flask.request.sid in USERS:
        user = USERS[flask.request.sid]
        USERS.pop(flask.request.sid)
    else:
        return
    display()
    if GAME is None or not GAME.active:
        DISPLAY.update(list(USERS.values()))
    else:
        GAME.remove_player(user)
    # let every user know when a user disconnects
    sio.emit("userDisconnected", flask.request.sid, broadcast=True)
    # print("dc " + request.sid)

# ----------------- Chat ------------------

CHATLOG = []

@SOCKETIO.on('sendToServer')
def send_to_server(data):
    if data["type"] == "chat":
        CHATLOG.append(data)
        # broadcast allows for all connected socket to receive the message
        sio.emit('chatLogFromServer', CHATLOG, broadcast=True)
    elif data["type"] == "chatLog":
        sio.emit('chatLogFromServer', CHATLOG, broadcast=True)
    elif data["type"] == "retrieveUsers":
        sio.emit('userList', USERS, broadcast=True)
    elif data["type"] == "retrieveUsername":
        sio.emit('username', USERS.get(flask.request.sid))

if __name__ == '__main__':
    SOCKETIO.run(APP, host="0.0.0.0", debug=True)
