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

def checkUser(userData):
    for username in userData:
        print(username)

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
    print(userInfo['username'])
    print(userInfo['socketId'])
    print(data + " has logged in")
    #checkUser(data)
    #emit('userValid', {'room': users})
    #emit('userInvalid', {'room': users})

# When the client disconnects from the socket
@socketio.on('disconnect')
def red():
    print("disconnected")

if __name__ == '__main__':
    socketio.run(app)