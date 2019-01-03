import React, { Component } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import UsernamePicker from './UsernamePicker';
import Room from './Room/Room';
import Double07 from './Games/Double07';
import HotPotato from './Games/Hot_Potato';
import Game3 from './Games/Game3';
import Game4 from './Games/Game4';
import Game5 from './Games/Game5';
import NotFound from './NotFound';
import io from 'socket.io-client';


class App extends Component {
    constructor(props) {
        super(props);

        this.state = {
            username: '',
            socket: '',
            gameList: []
        };

        this.socket = io('http://localhost:5000');
    }

    updateUsername = (username) => {
        this.setState({ username: username });
    };
    updateSocketId = (socketId) => {
        this.setState({ socketId: socketId });
    };
    updateGameList = (gameList) => {
        this.setState({ gameList: gameList });
    };

    render() {
        return (
            <BrowserRouter>
                <Switch>
                    <Route
                        exact
                        path="/"
                        render={(props) => <UsernamePicker {...props}
                        userState={this.state}
                        socket={this.socket}
                        updateUsername={this.updateUsername}
                        updateSocketId={this.updateSocketId}
                        updateGameList={this.updateGameList}
                        />} 
                    />
                    <Route
                        path="/room"
                        render={(props) => <Room {...props}
                        userState={this.state}
                        socket={this.socket}
                        />}
                    />
                    <Route
                        path="/Double07" 
                        render={(props) => <Double07 {...props}
                        userState={this.state}
                        socket={this.socket}
                        />}
                    />
                    <Route
                        path="/Hot_Potato"
                        render={(props) => <HotPotato {...props}
                        userState={this.state}
                        socket={this.socket}
                        />}
                    />
                    <Route path="/game3" component={Game3} />
                    <Route path="/game4" component={Game4} />
                    <Route path="/game5" component={Game5} />
                    <Route path="/" component={NotFound} />
                </Switch>
            </BrowserRouter>
        );
    }
}

export default App;
