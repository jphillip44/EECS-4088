import React from 'react';

class GameList extends React.Component {    
    render() {
        let sessionGames;
        if (this.props.gameList.length !== 0) {
            sessionGames = this.props.gameList;
        } else {
            sessionGames = sessionStorage.getItem('gameList').split(",");
        }
        return (
            <div className="box">
                <h1 className="title">Games</h1>
                <div className="content">
                    <div className="buttons">
                         {sessionGames.map((game, index) => (
                            <button
                                className="button"
                                key={index}
                                onClick={() => this.props.goToGame(game)}
                            >
                                {game}
                            </button>
                        ))}
                    </div>            
                </div>          
            </div>
        );
    }
}

export default GameList;