import React from 'react';

class GameList extends React.Component {    
    render() {
        return (
            <div className="box">
                <h1 className="title">Games</h1>
                <div className="content">
                    <div className="buttons">
                        {this.props.gameList.map((user, index) => (
                            <button
                                className="button"
                                key={index}
                                onClick={() => this.props.goToGame(user)}
                            >
                                {user}
                            </button>
                        ))}   
                    </div>            
                </div>          
            </div>
        );
    }
}

export default GameList;