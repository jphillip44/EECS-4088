import React from 'react';
import UsernameNotification from './UsernameNotification';

class UsernamePicker extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            username: '',
            socketId: ''    
        };

        this.usernameInput = React.createRef();

        this.props.socket.on('games', (data) => {
            this.props.updateGameList(data.games);
            console.log(data.games);
        });

        this.props.socket.on('username', (data) => {
            this.props.updateUsername(data);
            this.props.updateSocketId(this.props.socket.id);
            // Save username to localstorage for persistance
            window.localStorage.setItem('username', data);
            this.setState({
                username: data,
                socketId: this.props.socket.id
            });

            this.props.history.push("/room");
        });
    }

    // Submits user data to server and updates usernamePicker and app component state
    submitUsername = (event) => {
        event.preventDefault();
        this.props.socket.emit('joinServer', {
            username: this.usernameInput.current.value,
            socketId: this.props.socket.id  
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
                                    <form onSubmit={this.submitUsername}>
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