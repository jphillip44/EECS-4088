#!/usr/bin/python3
from threading import Thread
from flask import Flask, request, render_template
from flask_socketio import SocketIO, join_room, emit
import json

# import glob
# modules = glob.glob('games/*.py')
# from games import *
# from games import *
from games import *

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
    test = userInfo["username"]
    users[userInfo["socketId"]] = userInfo["username"] + " #" + userInfo["socketId"][:4]
    print(users.get(userInfo["socketId"])  + " has logged in")
    emit('username', {'username': users[userInfo["socketId"]]})
    if test == "454":
        game = Game1()
    else:
        game = Game2()
    game.foo()

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
# @socketio.on('disconnect')
def dc():
    del users[request.sid]

# @socketio.on('connect')
# def con():
#     # print("con " + request.sid)
#     gm = game.Start(socketio)


if __name__ == '__main__':
    # Thread(target=background).start()
    socketio.run(app, host="0.0.0.0")
    # wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)
