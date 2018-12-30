import React from 'react';
import UsernameNotification from './UsernameNotification';

class UsernamePicker extends React.Component {
    constructor(props) {
        super(props);
        this.usernameInput = React.createRef();
    }

    state = {
        username: '',
        socketId: ''
    };

    // Submits user data to server and updates usernamePicker and app component
    // state
    submitUsername = (event) => {
        event.preventDefault();
        // Save username to localstorage for persistance
        window.localStorage.setItem('username', this.usernameInput.current.value);

        this.props.updateUsername(this.usernameInput.current.value);

        this.setState({
            username: this.usernameInput.current.value,
            socketId: this.props.socket.id
        }, () => {
            this.props.socket.emit('joinServer', {
                username: this.state.username,
                socketId: this.props.socket.id
        
            });

            // Clear the username input field
            this.usernameInput.current.value = '';

            this.props.history.push("/room");
        });
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