import React from 'react';
import Hammer from 'hammerjs';

class Hot_Potato extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            timer: 0,
            potatoHolder: '',
            userTurn: false,
            explode: false,
            handImage: '/images/hand.png'
        };
    }
    
    componentDidMount() {
        // Setup swipe on swipePotato element
        let stage = document.getElementById('swipePotato');
        let mc = new Hammer(stage);
        mc.on("swipe", this.endOfTurn);

        // Initialize parameters in state, start timer, and set image to potato
        this.props.socket.on('state', (data) => {     
            if (this.props.userState.username === data.next) {
                this.setState({
                    userTurn: true,
                    timer: 0,
                    explode: false,
                    handImage: '/images/hand_with_potato.png'
                 }, () => {
                    this.interval = setInterval(() => this.updateTimer(), 1000);    
                });                
            }
            this.setState({ potatoHolder: data.next });
        });
        // On explode, switch users, reset timer and emit endOfTurn to server
        this.props.socket.on('explode', () => {
            clearInterval(this.interval);
            this.setState({
                userTurn: false,
                explode: true
            });
            this.props.socket.emit('endOfTurn', { "player": this.state.potatoHolder });
        });
        // When game is over, return to room page
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
        // emit the person that held the potato and the time they successfully held it 
        if (this.state.userTurn === true) {          
            this.props.socket.emit('endOfTurn', {
                "player": this.state.potatoHolder,
                "time": this.state.timer, 
            });
            // Reset hand image to empty on end of users 
            this.setState({
                userTurn: false,
                handImage: '/images/hand.png'
            });
            clearInterval(this.interval);
        }        
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
                                    <h6 className={this.state.userTurn === true ? "title is-6" : "is-hidden"}>
                                        Swipe Left or Right To Pass The Potato
                                    </h6>
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