#!/usr/bin/python3

from flask import Flask, request, render_template
from flask_socketio import SocketIO, join_room, emit
from uuid import uuid4
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
    userInfo["username"] += (" #" + uuid4().hex)
    print(userInfo["username"] + " has logged in")
    emit('username', {'username': userInfo["username"]})

# When the client disconnects from the socket
@socketio.on('disconnect')
def red():
    print("disconnected")

@socketio.on('connect')
def red():
    print("connected")

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0")