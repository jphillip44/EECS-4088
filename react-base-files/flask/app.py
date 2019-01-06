#!/usr/bin/python3
try:
    from eventlet import monkey_patch
    monkey_patch()
    print("Running Eventlet Server")
    async_mode='eventlet'
except ModuleNotFoundError:
    try:
        from gevent import monkey
        monkey.patch_all()
        print("Running Gevent Server")
        async_mode='gevent'
    except ModuleNotFoundError:
        print("Running Flask Server")
        async_mode = None

import json
import desktop
import threading

import flask_socketio as sio
import flask

from game_list import GameList
from display_game import DisplayGame

# initialize Flask

app = flask.Flask(__name__)
socketio = sio.SocketIO(app, async_mode=async_mode)

users = {}
game = None
game_thread = None
display_game = None

# This is a catch-all route, this allow for react to do client-side
# routing and stoping flasks routing
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return flask.render_template('index.html')

@socketio.on('joinServer')
def join_server(data):
    "Create a game lobby"
    users[data["socketId"]] = data["username"] + " #" + data["socketId"][:4]
    print(users.get(data["socketId"])  + " has logged in")   
    sio.emit('games', {'games': GameList.list_games()})
    sio.emit('username', {'username': users[data["socketId"]]})
    sio.join_room(users[data["socketId"]])
    global game
    display()
    if game is None or not game.active:
        DisplayGame.update([*users.values()])

@socketio.on('createGame')
def create_game(data):
    global game
    global display_game
    print(users)
    if display_game is None:
        display_game=DisplayGame()
    if game is None or not game.active:
        game = GameList.select_game(data, users.values(), socketio=socketio, display_game=display_game)
        sio.emit('gameStarted', game.__name__, broadcast=True)
        global game_thread
        if game_thread is None or not game_thread.isAlive():
            game_thread = threading.Thread(target=game.run_game)
            game_thread.start()

def display():
    print("users")
    print(*users.values(), sep='\n') if users else print('none')

# ----------------- Chat ------------------

chatLog = []

@socketio.on('sendToServer')
def send_to_server(data):
    if data["type"] == "chat":
        chatLog.append(data)
        # broadcast allows for all connected socket to receive the message
        sio.emit('chatLogFromServer', chatLog, broadcast=True)
    elif data["type"] == "chatLog":
        sio.emit('chatLogFromServer', chatLog, broadcast=True)
    elif data["type"] == "retrieveUsers":
        sio.emit('userList', users, broadcast=True)
    elif data["type"] == "retrieveUsername":
        sio.emit('username', users.get(flask.request.sid))

# When the client disconnects from the socket
@socketio.on('disconnect')
def dc():
    if users.get(flask.request.sid):
        del users[flask.request.sid]
    display()
    if game is None or not game.active:
        DisplayGame.update([*users.values()])
    # let every user know when a user disconnects
    sio.emit("userDisconnected", flask.request.sid, broadcast=True)
    # print("dc " + request.sid)

# @socketio.on('connect')
def con():
    print("con " + flask.request.sid) 
#     gm = game.Start(socketio)


if __name__ == '__main__':
    # game_thread(target=background).start()
    socketio.run(app, host="0.0.0.0")
    # wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)
