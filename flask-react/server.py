#!/usr/bin/python3

from flask import Flask, request, render_template
from flask_socketio import SocketIO, join_room, emit
import json

# initialize Flask
app = Flask(__name__)
socketio = SocketIO(app)
ROOMS = {} # dict to track active rooms

@app.route('/')
def index():
    """Serve the index HTML"""
    return render_template('index.html')

@socketio.on('create')
def on_create(data):
    """Create a game lobby"""
    print(data + " has logged in")
    room = 'controller'
    ROOMS[room] = 'controller'
    join_room(room)
    emit('join_room', {'room': room})

if __name__ == '__main__':
    socketio.run(app)