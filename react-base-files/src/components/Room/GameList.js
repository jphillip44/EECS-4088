import React from 'react';

class GameList extends React.Component {    
    render() {
        let localGames;
        if (this.props.gameList.length !== 0) {
            localGames = this.props.gameList;
        } else {
            localGames = localStorage.getItem('gameList').split(",");
        }
        return (
            <div className="box">
                <h1 className="title">Games</h1>
                <div className="content">
                    <div className="buttons">
                         {localGames.map((game, index) => (
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