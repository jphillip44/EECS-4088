#!/usr/bin/python3

from flask import Flask, request, render_template, session
from flask_socketio import SocketIO
from flask_socketio import send, emit
from flask_socketio import join_room, leave_room
import json

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)
users = {}
rooms = {}

@app.route('/')
def sessions():
    return render_template('index.html')

@app.route('/2/')
def sessions2():
    return render_template('index2.html')

@app.route('/cl/', methods=['POST'])
def cl_index():
    jsondata = request.get_json()
    data = json.loads(jsondata)
    print(data['input']['topic1'])
    print(data['input']['topic2'])

    result = {'escalate': True}
    return json.dumps(result) 

def messageReceived(methods=['GET', 'POST']):
    print(users)
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

@socketio.on('join')
def on_join(data):
    print("HALP!")
    username = data['username']
    room = data['room']
    join_room(room)
    print(username + ' has entered the room.', room=room)
    send(username + ' has entered the room.', room=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', room=room)
    print(username + ' has left the room.', room=room)



if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')