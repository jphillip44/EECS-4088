import React from 'react';
import Hammer from 'hammerjs';

class Hot_Potato extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            timeFromServer: 0,
            timer: 0,
            potatoHolder: '',
            userTurn: false,
            explode: false,
            handImage: '/images/hand.png'
        };
    }
    
    componentDidMount() {

        let stage = document.getElementById('swipePotato');
        let mc = new Hammer(stage);

        mc.on("swipe", this.endOfTurn);

        this.props.socket.on('state', (data) => {     
            if (this.props.userState.username === data.next) {
                this.setState({
                    userTurn: true,
                    explode: false,
                    handImage: '/images/hand_with_potato.png'
                 }, () => {
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
                timer: 0,
                explode: true
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
            timer: 0,
            handImage: '/images/hand.png'
        });
        this.props.socket.emit('endOfTurn', {
            "player": this.state.potatoHolder,
            "time": this.state.timer, 
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
                                    <img
                                        id="swipePotato" 
                                        src={this.state.explode === true ? "/images/hand_with_explosion.png" : this.state.handImage}
                                        alt="Pass Potato"
                                    />
                                    <button
                                        className="button is-primary is-fullwidth"
                                        onClick={this.endOfTurn}
                                        disabled={!this.state.userTurn}
                                    >
                                        Pass The Potato
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