#!/usr/bin/python3

from flask import Flask, request, render_template
from flask_socketio import SocketIO, join_room, emit
import json

# initialize Flask
app = Flask(__name__)
socketio = SocketIO(app)
ROOMS = {} # dict to track active rooms

users = []
chatlog = []

# This is a catch-all route, this allow for react to do client-side
# routing and stoping flasks routing
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

@socketio.on('create')
def on_create(data):
    """Create a game lobby"""
    print(data + " has logged in")
    users.append(data)
    room = 'controller'
    ROOMS[room] = 'controller'
    join_room(room)
    emit('join_room', {'room': users})

if __name__ == '__main__':
    socketio.run(app)