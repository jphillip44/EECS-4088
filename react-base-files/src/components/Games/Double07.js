import React from 'react';

class Double07 extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            allTargets: [],
            showTargets: false,
            showSingleTarget: false,
            action: 'reload',
            target: {},
            player: {},
        }
        // Wait for players data from server and convert it to list of players
        this.props.socket.on('state', (data) => {
            let keys = Object.keys(data)
            let targetList = [];
            let player = {};
            let i;
            for(i = 0; i < keys.length; i++) {
                if(keys[i] === this.props.userState.username) {
                    player = {
                        username: keys[i],
                        hp: data[keys[i]].hp,
                        ap:  data[keys[i]].ap    
                    };
                    console.log("PLAYER: " + player.username + " HP: " + player.hp + " AP: " + player.ap);
                } else {
                    targetList.push({
                        username: keys[i],
                        hp: data[keys[i]].hp,
                        ap: data[keys[i]].ap 
                    });
                    console.log("TARGET: " + keys[i] + " HP: " + data[keys[i]].hp + " AP: " + data[keys[i]].ap );
                }
            };

            this.setState({ allTargets: targetList });
            this.setState({ player: player });
        });

        this.props.socket.on('timerExpired', () => {
            this.props.socket.emit('endOfRound', {
                target: this.state.target.username,
                action: this.state.action,
                player: this.state.player.username
            });
            
            this.setState({
                action: 'reload',
                target: {},
                showSingleTarget: false
            });
        });
        
        this.props.socket.on('gameOver', () => {
            this.props.history.push(`/room`);
        });

        // Separate the entire player list into a target list and the user
        this.props.socket.on('allPlayers', (data) => {
            let i;
            let targetList = [];
            let player = {};
            for(i = 0; i < data.length; i++ ) {
                if(data[i].socketId !== this.props.socket.id) {
                    targetList.push(data[i]);
                } else {
                    player = data[i];
                }    
            };
            this.setState({ allTargets: targetList });
            this.setState({ player: player });
        });
    }

    // Used to be able to toggle selecting a targeted player
    choosePlayer = (user) => {
        let i;
        for(i = 0; i < this.state.allTargets.length; i++) {
            if(this.state.allTargets[i].username === user) {
                this.setState({
                    target: this.state.allTargets[i],
                    showTargets: false,
                    showSingleTarget: true
                });
            }
        }; 
    }

    chooseAction = (data) => {
        // Update showTargets so modal of targets pops up on screen
        if(data === "attack") {
            this.setState({
                action: data,
                showTargets: true
            });
        } else if (data === "defend" || data === "reload") {
            // Reset target when defend or reload is selected
            this.setState({
                action: data,
                showSingleTarget: false,
                target: {}
            });
        }    
    }
    
    render() {
        return (
            <div className="hero is-fullheight">
                <div className="hero-body">
                    <div className="container has-text-centered">
                        <div className="columns is-centered">
                            <div className="column is-5">
                                <h1 className="title is-1 has-text-white">007</h1>
                                <div className={this.state.showSingleTarget ? "box" : "box is-hidden"}>
                                    <h5 className="title is-5">Target</h5>
                                    <p>{this.state.target.username}</p>
                                </div>
                                <div className="box">
                                    <h5 className="title is-5">{this.props.userState.username}</h5>
                                    <div className="level is-mobile">
                                        <div className="level-item">
                                            <button className="button">Health Points: {this.state.player.hp}</button>
                                        </div>
                                        <div className="level-item">
                                            <button className="button">Action Points: {this.state.player.ap}</button>
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
                <div className={this.state.showTargets ? "modal is-active" : "modal"}>
                    <div className="modal-background"></div>
                        <div className="modal-content">
                            <div className="box has-text-centered">                                   
                                <h5 className="title is-5">Choose a Target</h5>
                                {this.state.allTargets.map((user, index) => (
                                    <div 
                                        className={this.state.target.username === user.username ? "button level is-mobile is-danger" : "button level is-mobile is-dark"}
                                        key={index}
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
                        </div>
                </div>
            </div>
        );
    }
}

export default Double07;