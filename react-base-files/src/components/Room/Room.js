import React from 'react';
import GameList from './GameList';
import ChatLog from './ChatLog';
import UserList from './UserList';

class Room extends React.Component {
    render() {
        return (
            <div className="hero is-fullheight">
                <div className="hero-body">
                    <div className="container">
                        <div className="columns is-centered">
                            <div className="column is-6 has-text-centered">
                                <h1 class="title is-1 has-text-white">Room</h1>
                                <GameList />
                                <ChatLog />
                                <UserList />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default Room;