import React from 'react';
import io from 'socket.io-client';

class UsernamePicker extends React.Component {
    constructor(props) {
        super(props);
        this.usernameInput = React.createRef();
        this.socket = io('http://localhost:5000');
    }

    state = {
        username: '',
        userValid: true,
        socketId: ''
      };

    componentDidMount() {
    // Username is valid, updates app and usernamepick state to true, and go
    // to /room
        this.socket.on('userValid', data => {
            this.setState({ userValid: data.userValid });
            this.props.updateUserValid(data.userValid);
            this.props.history.push("/room");
        });
    // Username is invalid, updates app and usernamepick state to false   
        this.socket.on('userInvalid', data => {
            this.setState({ userValid: data.userValid });
            this.props.updateUserValid(data.userValid);
        });

        this.socket.on('username', data => {
            console.log(data.username);
            this.props.history.push("/room");
        });
    }
    // Submits user data to server and updates usernamePicker and app component
    // state
    checkUsername = (event) => {
        event.preventDefault();
        this.props.updateUsername(this.usernameInput.current.value);
        this.props.updateUserValid(this.state.userValid);
        this.props.updateSocketId(this.socket.id);
        this.setState({
            username: this.usernameInput.current.value,
            socketId: this.socket.id
        }, () => {
            this.socket.emit('joinServer', JSON.stringify({
                username: this.state.username,
                socketId: this.state.socketId
            }));
        });
        
        // Clear the username input field
        this.usernameInput.current.value = '';
    } 

    render() {   
        return (
            <div className="hero is-fullheight">
                <div className="hero-body">
                    <div className="container has-text-centered">
                    <h1 className="landing title is-1 has-text-white">UI Tester</h1>
                    <h5 className="subtitle is-5 has-text-light">Where dreams go to die</h5>
                        <div className="columns is-centered">
                            <div className="column is-4">
                                <div className="box">
                                    <form onSubmit={this.checkUsername}>
                                        <label className="label">Pick your username</label>
                                        <div className="field">
                                            <div className="control">
                                                <div className="message is-danger is-small">
                                                    <div className="message-body">
                                                        {(this.state.userValid === false) ? `${this.state.username} is already being used` : ``}
                                                    </div>
                                                </div>
                                                <input
                                                    className="input"
                                                    type="text"
                                                    name="username"
                                                    placeholder="Username"
                                                    required
                                                    ref={this.usernameInput}
                                                />
                                            </div>  
                                        </div>
                                        <div className="field">
                                            <div className="control">
                                                <button 
                                                    type="submit"
                                                    className="button is-info is-fullwidth"
                                                >
                                                    Submit
                                                </button>
                                            </div>
                                        </div>
                                    </form>  
                                </div>                  
                            </div>
                        </div>
                    </div>
                </div>  
            </div>
        );
    }
}

export default UsernamePicker;