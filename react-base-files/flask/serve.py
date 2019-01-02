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

from flask import Flask, request, render_template
from flask_socketio import SocketIO, join_room, emit
from threading import Thread
import json

from gameList import GameList

# initialize Flask

app = Flask(__name__)
socketio = SocketIO(app)

users = {}
game = None
game_thread = None

# This is a catch-all route, this allow for react to do client-side
# routing and stoping flasks routing
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

@socketio.on('joinServer')
def join_server(data):
    "Create a game lobby"
    users[data["socketId"]] = data["username"] + " #" + data["socketId"][:4]
    print(users.get(data["socketId"])  + " has logged in")   
    emit('games', {'games': GameList.list_games()})
    emit('username', {'username': users[data["socketId"]]})
    join_room(users[data["socketId"]])  
    display()

@socketio.on('createGame')
def create_game(data):
    global game
    print(users)
    if game is None or not game.is_active():
        game = GameList.select_game(data, users.values(), socketio)
        emit('gameStarted', game.__name__, broadcast=True)
        global game_thread
        if game_thread is None or not game_thread.isAlive():
            game_thread = Thread(target=game.run_game)
            game_thread.start()

def display():
    print("users")
    print(*users.values(), sep='\n')

# ----------------- Chat ------------------

chatLog = []

@socketio.on('sendToServer')
def send_to_server(data):
    if data["type"] == "chat":
        chatLog.append(data)
        # broadcast allows for all connected socket to receive the message
        emit('chatLogFromServer', chatLog, broadcast=True)
    elif data["type"] == "chatLog":
        emit('chatLogFromServer', chatLog, broadcast=True)
    elif data["type"] == "retrieveUsers":
        emit('userList', users, broadcast=True)
    elif data["type"] == "retrieveUsername":
        emit('username', users[request.sid])

# When the client disconnects from the socket
@socketio.on('disconnect')
def dc():
    del users[request.sid]
    # let every user know when a user disconnects
    emit("userDisconnected", request.sid, broadcast=True)
    print("dc " + request.sid)

@socketio.on('connect')
def con():
    print("con " + request.sid) 
#     gm = game.Start(socketio)


if __name__ == '__main__':
    # game_thread(target=background).start()
    socketio.run(app, host="0.0.0.0")
    # wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)
