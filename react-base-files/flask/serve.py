#!/usr/bin/python3

from flask import Flask, request, render_template
from flask_socketio import SocketIO, join_room, emit
import json

# initialize Flask
app = Flask(__name__)
socketio = SocketIO(app)
ROOMS = {} # dict to track active rooms

users = {}
chatlog = {}

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
    print(users.get(userInfo["socketId"])  + " has logged in")
    emit('username', {'username': users[userInfo["socketId"]]})

# When the client disconnects from the socket
@socketio.on('disconnect')
def dc():
    print(users)

@socketio.on('connect')
def red():
    print("connected")

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0")