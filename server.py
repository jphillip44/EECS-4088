#!/usr/bin/python3

from flask import Flask, request, render_template
from flask_socketio import SocketIO, send, emit
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)
users = {}

@app.route('/cl/', methods=['POST'])
def cl_index():
    jsondata = request.get_json()
    data = json.loads(jsondata)
    print(data['input']['topic1'])
    print(data['input']['topic2'])

    result = {'escalate': True}
    return json.dumps(result) 

@app.route('/')
def sessions():
    return render_template('index.html')

@app.route('/test/')
def test():
    return '<h1>Hello World</h1>'



def messageReceived(methods=['GET', 'POST']):
    print(users)
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    user = json.get('user_name')
    if user:
        users[user] = 0
    print(users)
    socketio.emit('my response', json, callback=messageReceived)




if __name__ == '__main__':
    socketio.run(app)