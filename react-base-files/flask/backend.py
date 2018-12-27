#!/usr/bin/python3

from flask import Flask, request, render_template
from flask_socketio import SocketIO, join_room, emit
import json

# initialize Flask
app = Flask(__name__)
socketio = SocketIO(app)
ROOMS = {} # dict to track active rooms

users = []
chatLog = []

# This is a catch-all route, this allow for react to do client-side
# routing and stoping flasks routing
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

@socketio.on('connect')
def connect():
    print("Connected To Server")

@socketio.on('sendToServer')
def sendToServer(data):
    if data["type"] == "chat":
        chatLog.append(data)
        # broadcast allows for all connected socket to receive the message
        emit('chatMessageFromServer', chatLog, broadcast=True)
    elif data["type"] == "retrieveUsers":
        print("retrieveUsers: " + str(users))
        emit('userList', users, broadcast=True)
    elif data["type"] == "deleteUsers":
        # Check if the users list is empty
        if users:
            users.remove(data["username"])
        print(data["username"] + " deleted")
    elif data["type"] == "":
        print("TEST: " + data["username"])

@socketio.on('joinServer')
def joinServer(data):
    """Create a game lobby"""
    print(data["username"] + " has logged in")

    # check inputed username against users list on server, emit true for non 
    # duplicate name 
    for user in users:
        if user == data["username"]:
            print("Invalid Username")
            return emit("userValid", {"userValid": False})         
    print("Valid Username")
    users.append({
        "username": data["username"],
        "socketId": data["socketId"]
    })
    return emit("userValid", {"userValid": True})

# When the client disconnects from the socket
@socketio.on('disconnect')
def disconnect():
    print(request.sid + " disconnected")

# ----------------- 007 GAME ------------------

# opponents stores username, socket id, lives, action points of opponents
opponents = []
# player stores username, socket id, lives, action points of the player
player = {}
# actions stores each users actions in the current round
actions = []
# function endOfRound cycles through the actions list and applies those actions
# to players, updating players list

# broadcast is set to true so that when a user joins a game, it tells all other users
# in the game an updated opponents list
@socketio.on('initializeOpponentsStats')
def initializeOpponentsStats(data):
    # reset array on load
    opponents = []
    for user in users:
        if user["username"] != data:
            opponents.append({
                "username": user["username"],
                "socketId": user["socketId"],
                "hp": 3,
                "ap": 1
            })
    emit("opponentStats", opponents, broadcast=True) 

@socketio.on('initializeplayerStats')
def initializeplayerStats(data):
   for user in users:
        if user["username"] == data:
            print('SOCKETS MATCH')
            emit("playerStats", {
                "username": user["username"],
                "socketId": user["socketId"],
                "hp": 3,
                "ap": 1
            }) 

@socketio.on('endOfRound')
def endOfRound(data):
    print(data)


if __name__ == '__main__':
    socketio.run(app)