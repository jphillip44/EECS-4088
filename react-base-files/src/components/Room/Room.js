import React from 'react';
import GameList from './GameList';
import ChatLog from './ChatLog';
import UserList from './UserList';

class Room extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            username: '',
            users: [],
            chatLog: [],
        }
    }

    componentDidMount() {
        this.props.socket.emit('sendToServer', { type: 'retrieveUsers' });

        this.props.socket.emit('sendToServer', { type: 'retrieveUsername' });
        // Get chatlog when room loads
        this.props.socket.emit('sendToServer', { type: 'chatLog' });

        this.props.socket.on('username', (data) => this.setState({ username: data }));

        this.props.socket.on('gameStarted', (data) => { this.props.history.push(`/${data}`); });

        // When game is over, return to room page
        this.props.socket.on('gameOver', () => {
            console.log('gameover');
            this.props.history.push('/room');
        });

        // When the server disconnects, remove listeners and return to login page
        this.props.socket.on('disconnect', () => {
            console.log("disconnected")
            // this.props.socket.removeAllListeners();
            this.props.history.push('/room');
        });

        this.props.socket.on('reconnect', () => {
            console.log("reconnect")
            this.props.socket.emit('joinServer', {
                username: this.props.userState.username.split(" ")[0],
                socketId: this.props.socket.id  
            }); 
        });

        // gets the keys from the object returned from the server and loops through
        // the array using the previously gotten keys to get the values
        this.props.socket.on('userList', (data) => {
            let keys = Object.keys(data);
            let tempUsers = [];
            let i;
            for(i = 0; i < keys.length; i++) {
                tempUsers.push({
                    username: data[keys[i]],
                    socketId: keys[i]
                });
            };
            this.setState({ users: tempUsers });
        });

        this.props.socket.on('userDisconnected', (data) => {
            let tempUsers = [];
            let temp = this.state.users;
            let i;

            for(i = 0; i < this.state.users.length; i++) {
                if(temp[i].socketId !== data) {
                    tempUsers.push(temp[i]);
                }
            }         
            this.setState({ users: tempUsers });
        });

        this.props.socket.on('chatLogFromServer', (data) => {this.setState({ chatLog: data })});
    }

    sendMessage = (message) => {
        this.props.socket.emit('sendToServer', {
            type: 'chat',
            username: this.state.username,
            socketId: this.props.socket.id,
            message: message
        });
    };

    goToGame = (game) => {
        this.props.socket.emit('createGame', game);       
    };
    
    render() {
        return (
            <div className="hero is-fullheight">
                <div className="hero-body">
                    <div className="container">
                        <div className="columns is-centered">
                            <div className="column is-6 has-text-centered">                             
                                <GameList
                                    gameList={this.props.userState.gameList}
                                    goToGame={this.goToGame}
                                />
                                <ChatLog 
                                    sendMessage={this.sendMessage}
                                    chatLog={this.state.chatLog}
                                    username={this.state.username}
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