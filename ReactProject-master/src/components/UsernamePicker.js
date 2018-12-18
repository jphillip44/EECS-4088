import React from 'react';

class UsernamePicker extends React.Component {
    state = {
        username: ''
    };

    updateUsername = () => {
        console.log(this.state.username);
    };

    render() {   
        return (
            <div>
                <h2>Enter Your Username</h2>
                <input
                    type="text"
                    name="username"
                    placeholder="Username"
                    onChange={(event) => this.setState({ username: event.currentTarget.value })}
                />
                <button onClick={this.updateUsername} >
                    Submit
                </button>
            </div>
        );
    }
}

export default UsernamePicker;