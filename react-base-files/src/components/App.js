import React, { Component } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import UsernamePicker from './UsernamePicker';
import Room from './Room/Room';
import Game1 from './Games/Game1';
import Game2 from './Games/Game2';
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
      socket: this.socket
    };

    this.socket = io('http://localhost:5000', {
            'reconnection delay': 2500,
            'secure':true,
            'max reconnection attempts': 10,
            'reconnection':true       
        });
  }

  updateUsername = (username) => {
    this.setState({ username: username });
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
                path="/game1" 
                render={(props) => <Game1 {...props}
                userState={this.state}
                socket={this.socket}
                />}
              />
              <Route path="/game2" component={Game2} />
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
