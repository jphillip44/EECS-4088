import React from 'react';
import Game1 from '../Games/Game1';
import Game2 from '../Games/Game2';
import Game3 from '../Games/Game3';
import Game4 from '../Games/Game4';
import Game5 from '../Games/Game5';


class GameList extends React.Component { 
    render() {
        return (
            <div className="card">
                <header className="card-header">
                    <p className="card-header-title">Games</p>
                </header>
                <div className="card-content">
                    <Game1 />
                    <Game2 />
                    <Game3 />
                    <Game4 />
                    <Game5 /> 
                </div>          
            </div>
        );
    }
}

export default GameList;