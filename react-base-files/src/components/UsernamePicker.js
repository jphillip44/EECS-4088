import React from 'react';
import io from 'socket.io-client';
import UsernameNotification from './UsernameNotification';

class UsernamePicker extends React.Component {
    constructor(props) {
        super(props);
        this.usernameInput = React.createRef();
        this.socket = io('http://localhost:5000');
    }

    state = {
        username: '',
        userValid: null,
        socketId: ''
      };

    componentDidMount() {
    // Username is valid, updates app and usernamepick state to true, and go
    // to /room
        this.socket.on('userValid', data => {
            if(data.userValid) {
                console.log(1111111111111111111111);
                this.setState({ userValid: data.userValid });
                this.props.updateUserValid(data.userValid);

                this.props.history.push("/room");
            } else {
               console.log(222222222222222222);
                this.setState({ userValid: data.userValid });
                this.props.updateUserValid(data.userValid); 
            }          
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
    // Submits user data to server and updates usernamePicker and app component
    // state
    checkUsername = (event) => {
        event.preventDefault();
        // Save username to localstorage for persistance
        window.localStorage.setItem('username', this.usernameInput.current.value);

        this.props.updateUsername(this.usernameInput.current.value);
        this.props.updateUserValid(this.state.userValid);
        this.props.updateSocketId(this.socket.id);
        this.setState({
            username: this.usernameInput.current.value,
            socketId: this.socket.id
        }, () => {
            this.socket.emit('joinServer', {
                username: this.state.username,
                socketId: this.state.socketId
            });
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
                                                {this.state.userValid === false && <UsernameNotification />}
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
                                                <button type="submit" className="button is-info is-fullwidth">
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