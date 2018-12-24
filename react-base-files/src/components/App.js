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


class App extends Component {
  state = {
    username: '',
    userValid: false,
    socketId: ''
  };

  updateUsername = (username) => {
    this.setState({ username: username });
  };

  updateUserValid = (userValid) => {
    this.setState({ userValid: userValid });
  };

  updateSocketId = (socketId) => {
    this.setState({ socketId: socketId });
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
                  updateUsername={this.updateUsername}
                  updateUserValid={this.updateUserValid}
                  updateSocketId={this.updateSocketId}  
                />} 
              />
              <Route
                path="/room"
                render={(props) => <Room {...props}
                  userState={this.state}
                />}
              />
              <Route path="/game1" component={Game1} />
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
