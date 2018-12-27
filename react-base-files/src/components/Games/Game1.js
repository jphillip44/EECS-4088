import React from 'react';
import io from 'socket.io-client';

class Game1 extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            users: [],
            opponents: [],
            action: '',
            target: '',
            player: {},
            hp: '',
            ap: '',
            timeLeft: 15
        }
        this.socket = io('http://localhost:5000'); 
        this.socket.on('clients', (data) => {
            console.log(data + " : " + this.socket.id);
        });
        
        this.socket.on('userList', (data) => {
            this.setState({ users: data });
        });
        
        this.socket.on('opponentStats', (data) => {
            console.log("Opponent Stats: " + data);
            this.setState({ opponents: data });
        });

        this.socket.on('playerStats', (data) => {
            console.log("Player Stats: " + data);
            this.setState({ player: data });
        });

        this.socket.on('updateTimer', (data) => {
            this.setState({ timeLeft: data });
        });
    }

    componentDidMount() {
        this.socket.emit('sendToServer', {
            type: 'retrieveUsers',
            username: window.localStorage.getItem('username'),
            socketId: this.socket.id,
            message: "" 
        });

        this.socket.emit('initializeOpponentsStats', window.localStorage.getItem('username'));
        this.socket.emit('initializeplayerStats', window.localStorage.getItem('username'));
    }

    componentWillUnmount() {
        this.socket.emit('sendToServer', {
            type: 'deleteUsers',
            username: window.localStorage.getItem('username'),
            socketId: this.socket.id,
            message: "" 
        });
        console.log('DELETE');
    }

    sendActionToServer = (action) => {
        this.socket.emit("sendActionToServer", {
            action: action,
            username: window.localStorage.getItem('username'),
            socketId: this.socket.id,
            message: "" 
        });
    }
    // Used to be able to toggle selecting a targeted player
    choosePlayer = (user) => {
        if(this.state.target === user) {
            this.setState({ target: '' });
        } else {
            this.setState({ target: user });
        }   
    }

    chooseAction = (data) => {
        this.setState({ action: data });
    }

    endOfRound = (data) => {
        this.socket.emit('endOfRound', {
            target: this.state.target,
            action: this.state.action,
            user: window.localStorage.getItem('username')
        });
        
        this.setState({
            action: '',
            target: '',
            timeLeft: 15
        });
    }
    
    render() {
        return (
            <div className="hero is-fullheight">
                <div className="hero-body">
                    <div className="container has-text-centered">
                        <div className="columns is-centered">
                            <div className="column is-5">
                            <button onClick={this.endOfRound}>End of Round</button>
                                <div className="box">                                   
                                    <h5 className="title is-5">Players</h5>
                                    {this.state.opponents.map((user) => (
                                        <div 
                                            className={this.state.target === user.username ? "button level is-mobile is-danger" : "button level is-mobile is-dark"}
                                            key={user.socketId}
                                            onClick={() => this.choosePlayer(user.username)}
                                        >
                                            <div className="level-item">
                                                <span>{user.username}</span>
                                            </div>
                                            <div className="level-item">
                                                <span>{user.hp} Hp</span>
                                            </div>
                                            <div className="level-item">
                                                <span>{user.ap} AP</span>  
                                            </div>                                          
                                        </div> 
                                    ))} 
                                </div>
                                <div className="box">
                                    <h5 className="title is-5">{window.localStorage.getItem('username')}</h5>
                                    <div className="level is-mobile">
                                        <div className="level-item">
                                            <button className="button">Hp: {this.state.player.hp}</button>
                                        </div>
                                        <div className="level-item">
                                            <button className="button">Ap: {this.state.player.ap}</button>
                                        </div>
                                        <div className="level-item">
                                            <button className="button">Time Left: {this.state.timeLeft}</button>
                                        </div>
                                    </div>
                                </div>
                                <div className="box">
                                    <div className="buttons">
                                        <button
                                            className={this.state.action === "attack" ? "button is-fullwidth is-danger" : "button is-fullwidth is-dark"}
                                            onClick={() => this.chooseAction("attack")}>
                                            Attack
                                        </button>
                                        <button
                                            className={this.state.action === "defend" ? "button is-fullwidth is-danger" : "button is-fullwidth is-dark"}
                                            onClick={() => this.chooseAction("defend")}>
                                            Defend
                                        </button>
                                        <button
                                            className={this.state.action === "reload" ? "button is-fullwidth is-danger" : "button is-fullwidth is-dark"}
                                            onClick={() => this.chooseAction("reload")}>
                                            Reload
                                        </button>
                                    </div>
                                    
                                </div>                  
                            </div>
                        </div>
                    </div>
                </div>  
            </div>
        );
    }
}

export default Game1;