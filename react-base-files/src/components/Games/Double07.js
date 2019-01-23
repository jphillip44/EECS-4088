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
    }

    componentDidMount() {
        // Wait for players data from server and convert it to list of players
        this.props.socket.on('state', (data) => {
            // reset state to default values
            this.setState({
                target: {},
                targetList: [],
                showSingleTarget: false,
                showTargets: false
            }, () => {
                console.log('state');
                console.log(data);
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
                    } else {
                        // Remove player from targetList if hp = dead
                        if (data[keys[i]].hp === "dead") {                          
                        } else {
                            targetList.push({
                                username: keys[i],
                                hp: data[keys[i]].hp,
                                ap: data[keys[i]].ap 
                            });     
                        }
                    }
                };
                // Reset button to reload after attack in previous round
                if (this.state.action === 'attack' && Object.keys(this.state.target).length === 0) {
                    this.setState({
                        action: 'reload'
                    });
                }

                // Switch to reload action when user ap is zero
                if (player.ap === 0) {
                    this.setState({
                        allTargets: targetList,
                        player: player,
                        action: 'reload'
                    });
                } else {
                    this.setState({
                        allTargets: targetList,
                        player: player,
                    });
                }
            });
        });

        this.props.socket.on('timerExpired', () => {
            console.log('timerExpired');
            // Only emit user state to server when player is alive
            if (!(this.state.player.hp === "dead")) {
                // If attack is picked but not a target, default to reload
                if (this.state.action === 'attack' && Object.keys(this.state.target).length === 0) {
                    this.props.socket.emit('endOfRound', {
                        target: this.state.target.username,
                        action: 'reload',
                        player: this.state.player.username
                    });
                    this.setState({ action: 'reload' });
                } else {
                    this.props.socket.emit('endOfRound', {
                        target: this.state.target.username,
                        action: this.state.action,
                        player: this.state.player.username
                    });
                }
            }     
        });

        window.addEventListener('beforeunload', this.onPageRefresh);

        this.afterPageRefresh(sessionStorage.getItem('pageRefreshed'));
    }

    componentWillUnmount() {
        this.props.socket.removeAllListeners();
    }

    // Store state in local storage
    onPageRefresh = () => {
        this.props.socket.emit('refresh');
        sessionStorage.setItem('state', JSON.stringify(this.state));
        sessionStorage.setItem('pageRefreshed', 'true');
    };

    afterPageRefresh = (refreshed) => {
        if (refreshed === 'true') {
            console.log('AfterPageRefresh');
            sessionStorage.setItem('pageRefreshed', 'false');
            let sessionState = JSON.parse(sessionStorage.getItem('state'));
            this.setState(sessionState);
        }
    }

    // Used to be able to toggle selecting a targeted player
    choosePlayer = (user) => {
        let i;
        for(i = 0; i < this.state.allTargets.length; i++) {
            if(this.state.allTargets[i].username === user) {
                this.setState({
                    action: 'attack',
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
                // action: data, Fix server crash when round ends before target selection
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

    closeTargetList = () => {
        this.setState({ showTargets: false });
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
                                    <h5 className="title is-5">{sessionStorage.getItem('username')}</h5>
                                    <div className="level">
                                        <div className="level-item">
                                            <span className="button is-white">HP: {this.state.player.hp}</span>
                                            {this.state.player.hp > 0 && <span className="level-item"><img src="/images/double07/heart.png" alt="Heart" /> </span>}
                                            {this.state.player.hp > 1 && <span className="level-item"><img src="/images/double07/heart.png" alt="Heart" /> </span>}
                                            {this.state.player.hp > 2 && <span className="level-item"><img src="/images/double07/heart.png" alt="Heart" /></span>}
                                        </div>
                                        <div className="level-item">
                                            <button className="button is-white">Action Points: {this.state.player.ap}</button>
                                        </div>
                                    </div>
                                </div>
                                <div className="box">
                                    <div className="buttons">
                                        <button
                                            className={this.state.action === "attack" ? "button is-fullwidth is-danger" : "button is-fullwidth is-dark"}
                                            onClick={() => this.chooseAction("attack")}
                                            disabled={this.state.player.ap === 0 || this.state.player.hp === "dead"}
                                        >
                                            Attack
                                        </button>
                                        <button
                                            className={this.state.action === "defend" ? "button is-fullwidth is-danger" : "button is-fullwidth is-dark"}
                                            onClick={() => this.chooseAction("defend")}
                                            disabled={this.state.player.ap === 0 || this.state.player.hp === "dead"}
                                        >
                                            Defend
                                        </button>
                                        <button
                                            className={this.state.action === "reload" ? "button is-fullwidth is-danger" : "button is-fullwidth is-dark"}
                                            onClick={() => this.chooseAction("reload")}
                                            disabled={this.state.player.ap === 0 || this.state.player.hp === "dead"}
                                        >
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
                            <div className="columns is-centered">
                                <div className="column is-7">
                                    <h5 className="title is-5">Choose a Target</h5>
                                    {this.state.allTargets.map((user, index) => (
                                        <div 
                                            className={this.state.target.username === user.username ? "button level is-mobile is-danger" : "button level is-mobile is-dark"}
                                            key={index}
                                            onClick={() => this.choosePlayer(user.username)}
                                        >
                                            <div className="level-left">
                                                <div className="level-item">
                                                    <span>{user.username}</span>                                       
                                                </div>
                                                <div className="level-item">
                                                    <span>HP: {user.hp} </span>     
                                                </div>
                                            </div>
                                            <div className="level-right">
                                                {user.hp > 0 && <span className="level-item"><img src="/images/double07/heart.png" alt="Heart" /></span>}
                                                {user.hp > 1 && <span className="level-item"><img src="/images/double07/heart.png" alt="Heart" /></span>}
                                                {user.hp > 2 && <span className="level-item"><img src="/images/double07/heart.png" alt="Heart" /></span>} 
                                            </div>                                           
                                        </div>
                                    ))}
                                </div>
                            </div>  
                        </div>
                    </div>
                    <button className="modal-close is-large" aria-label="close" onClick={this.closeTargetList}></button>
                </div>
                    
            </div>
        );
    }
}

export default Double07;