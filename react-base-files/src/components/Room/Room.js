import React from 'react';
import GameList from './GameList';
import ChatLog from './ChatLog';
import UserList from './UserList';
import io from 'socket.io-client';

class Room extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            users: [],
            chatLog: []
        }

        this.socket = io('http://localhost:5000');

        this.socket.on('clients', (data) => {
            console.log(data + " : " + this.socket.id);
        });
        
        this.socket.on('userList', (data) => {
            console.log("UserList: " + data);
            this.setState({ users: data });
        });

        this.socket.on('chatMessageFromServer', (data) => {
            console.log("chatMessageFromServer: " + data);
            this.setState({ chatLog: data });
        });
    }

    componentDidMount() {
        this.socket.emit('sendToServer', {
            type: 'retrieveUsers',
            username: window.localStorage.getItem('username'),
            socketId: this.socket.id,
            message: "" 
        });
    }

    componentWillUnmount() {
        this.socket.emit('sendToServer', {
            type: 'deleteUsers',
            username: window.localStorage.getItem('username'),
            socketId: this.socket.id,
            message: "" 
        });
        console.log('DELETE');
    }

    sendMessage = (message) => {
        this.socket.emit('sendToServer', {
            type: 'chat',
            username: window.localStorage.getItem('username'),
            socketId: this.socket.id,
            message: message
        });
    };
    
    render() {
        return (
            <div className="hero is-fullheight">
                <div className="hero-body">
                    <div className="container">
                        <div className="columns is-centered">
                            <div className="column is-6 has-text-centered">
                                <h1 className="title is-1 has-text-white">Room</h1>                               
                                <GameList />
                                <ChatLog 
                                    sendMessage={this.sendMessage}
                                    chatLog={this.state.chatLog}
                                />
                                <UserList users={this.state.users} />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default Room;