import React from 'react';
import { Link } from 'react-router-dom';

class GameList extends React.Component {    
    render() {
        return (
            <div className="box">
                <h1 className="title">Games</h1>
                <div className="content">
                    <div className="buttons">
                        {this.props.gameList.map((user, index) => (
                            <Link
                                className="button"
                                key={index}
                                onClick={() => this.props.goToGame(user)}
                                to={`/user`}
                            >
                                {user}
                            </Link>
                        ))}   
                    </div>            
                </div>          
            </div>
        );
    }
}

export default GameList;