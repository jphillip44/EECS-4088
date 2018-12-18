import React from 'react';
import io from 'socket.io-client';

class Reply extends React.Component {
    constructor(props) {
        super(props);
        this.socket = io('http://localhost:5000'); 
    }  
 
    componentDidMount() {
        this.socket.on('join_room', data => {
            this.updateMessage(JSON.stringify(data));
        })
    }
    
    connectToFlask = () => {
        this.socket.emit('create', this.props.username);
    }     
    updateMessage = (message) => {
        this.props.updateMessage(message);
    };

    render() {
        return (
            <div>
                <h1>Form Values</h1>
                <h2>{this.props.username} {this.props.password}</h2>
                <button onClick={this.connectToFlask}>CONNECT TO FLASK</button>
                <h1>Websocket Response</h1>
                <h2>{this.props.message}</h2>
            </div>
        );
    }
}

export default Reply;