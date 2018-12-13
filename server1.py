#!/usr/bin/python3

from flask import Flask, request, render_template
from flask_socketio import SocketIO, send, emit
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/test/')
def front():
    return '<h1>Hello World</h1>'

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@app.route('/cl/', methods=['POST'])
def cl_index():
    jsondata = request.get_json()
    data = json.loads(jsondata)
    print(data['input']['topic1'])
    print(data['input']['topic2'])

    result = {'escalate': True}
    return json.dumps(result) 

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)


if __name__ == '__main__':
    socketio.run(app)