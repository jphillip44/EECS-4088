#!/usr/bin/python3
# from eventlet import monkey_patch
# monkey_patch()

from threading import Thread
from flask import Flask, request, render_template
from flask_socketio import SocketIO, join_room, emit
import json

from gameList import GameList

# initialize Flask
app = Flask(__name__)
socketio = SocketIO(app)
ROOMS = {} # dict to track active rooms

users = {}
chatlog = {}
clients = []

# This is a catch-all route, this allow for react to do client-side
# routing and stoping flasks routing
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')


@socketio.on('joinServer')
def joinServer(data):
    """Create a game lobby"""
    userInfo = json.loads(data)
    users[userInfo["socketId"]] = userInfo["username"] + " #" + userInfo["socketId"][:4]
    emit('username', {'username': "test"})
    print(users.get(userInfo["socketId"])  + " has logged in")
    emit('username', {'username': users[userInfo["socketId"]]})
    emit('games', {'games': GameList().list_games()})
    if userInfo["username"] == '454':
        g = "Double07"
    else:
        g = "Hot_Potatoe"
    GameList.select_game(g, list(users.values())).play()
    print(GameList().list_games())

@socketio.on('createGame')
def createGame(data):
    global game
    game = GameList().select_game(data)

def background():
    i = 0
    while True:
        print(i)
        i += 1
        socketio.sleep(1)
        # emit('poll', broadcast=True)

# @socketio.on('pollResponse')
# def polling():
#     print("a")

# When the client disconnects from the socket
@socketio.on('disconnect')
def dc():
    # del users[request.sid]
    print("dc " + request.sid)

@socketio.on('connect')
def con():
    print("con " + request.sid) 
#     gm = game.Start(socketio)


if __name__ == '__main__':
    # Thread(target=background).start()
    socketio.run(app, host="0.0.0.0")
    # wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)
