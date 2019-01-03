import React from 'react';

class Hot_Potato extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            timeFromServer: 0,
            timer: 0,
            potatoHolder: '',
            userTurn: false
        };
    }
    
    componentDidMount() {
        this.props.socket.on('state', (data) => {     
            if (this.props.userState.username === data.next) {
                this.setState({ userTurn: true }, () => {
                    this.interval = setInterval(() => this.updateTimer(), 1000);    
                });                
            }
            this.setState({
                timeFromServer: data.timer,
                startTime: Date.now(),
                potatoHolder: data.next
            });
        });

        this.props.socket.on('explode', () => {
            clearInterval(this.interval);
            this.setState({
                userTurn: false,
                timer: 0
            });
            this.props.socket.emit('endOfTurn', { "player": this.state.potatoHolder });
        });

        this.props.socket.on('gameOver', () => {
            this.props.history.push('/room');
        });
    }

    componentWillUnmount() {
        this.props.socket.removeAllListeners();
    }

    updateTimer = () => {
        this.setState({ timer: this.state.timer + 1 });
    }

    endOfTurn = () => {
        this.setState({
            userTurn: false,
            timer: 0
        });
        this.props.socket.emit('endOfTurn', {
            "player": this.state.potatoHolder,
            "time": this.state.timer
        });
        clearInterval(this.interval);
    }

    render() {
        return (
            <div className="hero is-fullheight">
                <div className="hero-body">
                    <div className="container has-text-centered">
                        <div className="columns is-centered">
                            <div className="column is-5">
                                <h1 className="landing title is-1 has-text-white">Hot Potato</h1>
                                <div className={this.state.userTurn ? "box" : "box is-hidden"}>
                                    <h3 className="title is-3">Time Held</h3>
                                    <h5 className="title is-5">{this.state.timer} Seconds</h5>
                                </div>
                                <div className={this.state.userTurn ? "box is-hidden" : "box"}>
                                    <h3 className="title is-3">Player with Potato</h3>
                                    <h5 className="title is-5">{this.state.potatoHolder}</h5>
                                </div>
                                <div className="box">
                                    <button
                                        className="button is-primary is-fullwidth"
                                        onClick={this.endOfTurn}
                                        disabled={!this.state.userTurn}
                                    >
                                        Pass Potato
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>  
            </div>
        );
    }
}

export default Hot_Potato;