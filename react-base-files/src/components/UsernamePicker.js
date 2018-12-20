import React from 'react';
import io from 'socket.io-client';

class UsernamePicker extends React.Component {
    constructor(props) {
        super(props);
        this.usernameInput = React.createRef();
        this.socket = io('http://localhost:5000');
    }

    componentDidMount() {
        this.socket.on('join_room', data => {
            console.log(JSON.stringify(data));
        })
    }

    checkUsername = (event) => {
        event.preventDefault();
        this.props.updateUsername(this.usernameInput.current.value);
        this.props.updateSocketId(this.socket.id);
        this.socket.emit('joinServer', JSON.stringify({
            username: this.usernameInput.current.value,
            socketId: this.socket.id
        }));
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