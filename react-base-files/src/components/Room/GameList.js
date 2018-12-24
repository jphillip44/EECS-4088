import React from 'react';
import { Link } from 'react-router-dom';

class GameList extends React.Component { 
    render() {
        return (
            <div className="box">
                <h1 className="title">Games</h1>
                <div className="content">
                    <Link to="/Game1">Game1</Link>
                    <Link to="/Game2">Game2</Link>
                    <Link to="/Game3">Game3</Link>
                    <Link to="/Game4">Game4</Link>
                    <Link to="/Game5">Game5</Link>
                </div>          
            </div>
        );
    }
}

export default GameList;