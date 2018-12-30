#!/usr/bin/python3
from eventlet import monkey_patch
monkey_patch()

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

# This is a catch-all route, this allow for react to do client-side
# routing and stoping flasks routing
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')


@socketio.on('joinServer')
def joinServer(data):
    "Create a game lobby"
    users[data["socketId"]] = data["username"] + " #" + data["socketId"][:4]
    print(users.get(data["socketId"])  + " has logged in")
    emit('username', {'username': users[data["socketId"]]})
    emit('games', {'games': GameList.list_games()})

@socketio.on('createGame')
def createGame(data):
    global game
    print(users)
    if data == '007':
        temp = "Double07"
    if data == 'Hot Potato':
        temp = "Hot_Potato"
    game = GameList.select_game(temp, users.values())
    emit('gameStarted', game.__name__)
    runGame()

def runGame():
    while game.is_active():
        emit('state', game.get_state())
        for i in range(game.get_timer(), 0, -1):
            print(i)
            socketio.sleep(1)
        if game.get_timer():
            emit('timerExpired', "")
            print("Waiting for inputs")
            socketio.sleep(5)
            print("Times up")
        game.end_round()
        game.display()
    else:
        emit('gameOver', "")


@socketio.on('endOfRound')
def action(data):
    print(data)
    if game.action(data):
        emit('action', "")

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

# ----------------- Chat ------------------

chatLog = []

@socketio.on('sendToServer')
def sendToServer(data):
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

# ----------------- 007 GAME ------------------

# players stores username, socket id, lives, action points of all players
players = {}
# actions stores each users actions in the current round
actions = []
# function endOfRound cycles through the actions list and applies those actions
# to players, updating players list

# broadcast is set to true so that when a user joins a game, it tells all other users
# in the game an updated opponents list

@socketio.on('initializePlayers')
def initializePlayers():
    # reset array on load
    players = []
    for user in users:
        players.append({
            "username": users[user],
            "socketId": user,
            "hp": 3,
            "ap": 1
        })
    emit("allPlayers", players, broadcast=True) 

@socketio.on('endOfRound')
def endOfRound(data):
    print(data)

# ---------------- HOT POTATO GAME ------------------

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
    # Thread(target=background).start()
    socketio.run(app, host="0.0.0.0")
    # wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)
