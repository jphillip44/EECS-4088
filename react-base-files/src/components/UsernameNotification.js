import React from 'react';

class UsernameNotification extends React.Component {
    render() {
        return (
            <div className="message is-danger is-small">
                <div className="message-body">
                    {window.localStorage.getItem('username')} is already being used
                </div>
            </div>
        );
    }
}

export default UsernameNotification;