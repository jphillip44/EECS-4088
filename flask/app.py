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
        print("Running Flask non-production Server")

import threading
import flask
import flask_socketio as sio

import desktop
from game_list import GameList
from display_game import DisplayGame
from instructions import Instructions

# initialize Flask

APP = flask.Flask(__name__)
SOCKETIO = sio.SocketIO(APP)

USERS = {}
GAME = None
THREAD = None
DISPLAY = DisplayGame()
INSTRUCTIONS = False
# This is a catch-all route, this allow for react to do client-side
# routing and stoping flasks routing
@APP.route('/', defaults={'path': ''})
@APP.route('/<path:path>')
def index(path):
    '''
    Landing page for the app.
    '''
    return flask.render_template('index.html')

@SOCKETIO.on('joinServer')
def join_server(data):
    '''
    Routine for connecting to the server as a player.
    '''
    print(data['username'])
    USERS[flask.request.sid] = data["username"] + "/" + flask.request.sid[:3]
    print(USERS.get(flask.request.sid)  + " has logged in")
    sio.emit('games', {'games': GameList.list_games()})
    sio.emit('username', USERS[flask.request.sid])
    sio.join_room(USERS[flask.request.sid])
    global GAME
    display()
    global DISPLAY
    global INSTRUCTIONS
    if not INSTRUCTIONS and DISPLAY is not None and (GAME is None or not GAME.active):
        DISPLAY.update(Players())

@SOCKETIO.on('createGame')
def create_game(data):
    '''
    Launches a game in a seperate thread.
    '''
    global GAME
    global THREAD
    print(USERS)
    if GAME is None or not GAME.active:
        THREAD = threading.Thread(target=launch_game, args=[data]).start()
        sio.emit('gameStarted', data, broadcast=True)


def launch_game(data):
    print(data)
    global GAME
    global INSTRUCTIONS
    INSTRUCTIONS = True
    DISPLAY.update(Instructions().get(data))
    SOCKETIO.sleep(25)
    INSTRUCTIONS = False
    GAME = GameList.select_game(data, list(USERS.values()), \
        socketio=SOCKETIO, display_game=DISPLAY)
    GAME.run_game()
    threading.Thread(target=check_thread).start()
        
def check_thread():
    '''
    Used to check if the game thread has died and alerts the GUI.
    '''
    THREAD.join()
    SOCKETIO.sleep(10)
    DISPLAY.update(Players())

def display():
    '''
    Displays user list to the console.
    '''
    if USERS:
        print(list(USERS.values()))

# When the client disconnects from the socket
@SOCKETIO.on('disconnect')
def disconnect():
    '''
    Handles server disconnect.
    '''
    if flask.request.sid in USERS:
        user = USERS[flask.request.sid]
        USERS.pop(flask.request.sid)
    else:
        return
    display()
    global INSTRUCTIONS
    if not INSTRUCTIONS and GAME is None:
        DISPLAY.update(Players())
    else:
        GAME.remove_player(user)
    # let every user know when a user disconnects
    sio.emit("userDisconnected", flask.request.sid, broadcast=True)
    # print("dc " + request.sid)

@SOCKETIO.on('refresh')
def refresh():
    if flask.request.sid in USERS:
        user = USERS[flask.request.sid]
        if GAME is not None and GAME.active:
            GAME.add_player(user)



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

class Players():
    def __init__(self):
        '''
        The Players object is used by the display_game class to display users.
        Its functionally a wrapper for a list but exists as to define a function that
        expects a "Players" obect vs a "list" object which is a common class.
        '''
        self.players = list(USERS.values())

    def get(self):
        return self.players

if __name__ == '__main__':
    SOCKETIO.run(APP, host="0.0.0.0", debug=False)
