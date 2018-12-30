import React from 'react';
import { Link } from 'react-router-dom';

class GameList extends React.Component {    
    render() {
        return (
            <div className="box">
                <h1 className="title">Games</h1>
                <div className="content">
                    <div className="buttons">
                        <Link 
                            className="button" 
                            onClick={() => this.props.goToGame("007")} 
                            to="/Game1">007
                        </Link>
                        <Link 
                            className="button" 
                            onClick={() => this.props.goToGame("Hot Potato")} 
                            to="/Game2">Hot Potato
                        </Link>
                        <Link 
                            className="button" 
                            onClick={() => this.props.goToGame("game3")} 
                            to="/Game3">Game3
                        </Link>
                        <Link 
                            className="button" 
                            onClick={() => this.props.goToGame("game4")} 
                            to="/Game4">Game4
                        </Link>
                        <Link 
                            className="button" 
                            onClick={() => this.props.goToGame("game5")} 
                            to="/Game5">Game5
                        </Link>    
                    </div>            
                </div>          
            </div>
        );
    }
}

export default GameList;