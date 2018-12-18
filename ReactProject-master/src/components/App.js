import React, { Component } from 'react';
import '../App.css';
import UsernamePicker from './UsernamePicker';
import Reply from './Reply';

class App extends Component {
  state = {
    username: ''
  };

  updateUsername = (username) => {
    this.setState({ username: username });
  };

  render() {
    return (
      <div className="App">
        <UsernamePicker
          updateUsername={this.updateUsername}
        />
        <Reply
          updateMessage={this.updateMessage}
          message={this.state.message}
          username={this.state.username}
          password={this.state.password}
         />
      </div>
    );
  }
}

export default App;
