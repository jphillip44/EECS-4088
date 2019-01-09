import React from 'react';

class Match extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            direction: '',
            flip: false,
            playersTurn: false,
            cursor: [],
            cardValue: ''
        };
    }

    componentDidMount() {
        this.props.socket.on('turn', (data) => {
            // if next in state is the clients username
            if (data.next[0] === this.props.userState.username) {
                this.setState({
                    playersTurn: true,
                    cursor: [data.cursor[ 0], data.cursor[1]]
                });
            } else {
                this.setState({ playersTurn: false });
            }
            console.log(data);
        });

        this.props.socket.on('flip', (data) => {
            console.log('flip');
            this.interval = setInterval(() => this.flipCard(), 5000);
            this.setState({
                flip: true,
                playersTurn: false
            });
        });

        this.props.socket.on('cursor', (data) => {
            console.log('cursor');
            console.log(data);
        });

        this.props.socket.on('timeout', (data) => {
            console.log('timeout');
        });
    }

    submitDirection = (direction) => {       
        this.setState({ direction: direction }, () => {
            this.props.socket.emit(`${this.state.direction}`);
            console.log(`${this.state.direction}`);    
        });      
    }

    selectCard = () => {
        console.log("SELECT");
        this.props.socket.emit('select');
    }

    flipCard = () => {
        clearInterval(this.interval);
        this.setState({ flip: false });
    }
    
    render() {
        return (
            <div className="hero is-fullheight">
                <div className="hero-body">
                    <div className="container has-text-centered">
                        <div className="columns is-centered">
                            <div className="column is-5">
                                <h1 className="landing title is-1 has-text-white">Match</h1>
                                <div className="box">
                                    <h1 className="title is-1">
                                        {this.state.flip === true ? "CARD VALUE" : "CARD HIDDEN"}
                                    </h1>
                                </div>
                                <div className="box">
                                    <img src={"/images/hand.png"} alt ="RED"/>
                                </div>
                                <div className="box">
                                    <div className="field is-grouped is-grouped-centered">
                                        <div className="control">
                                            <button className="button is-large noButton" disabled></button>
                                        </div>
                                        <div className="control">
                                            <button
                                                className="button is-info is-large"
                                                disabled={this.state.playersTurn === false}
                                                onClick={() => this.submitDirection("up")}
                                            >
                                                <img src={"/images/up_chevron.png"} alt="UP" />
                                            </button>
                                        </div>
                                        <div className="control">
                                            <button className="button is-large noButton" disabled></button>
                                        </div>
                                    </div>
                                    <div className="field is-grouped is-grouped-centered">
                                        <div className="control">
                                            <button
                                                className="button is-info is-large"
                                                disabled={this.state.playersTurn === false}
                                                onClick={() => this.submitDirection("left")}
                                            >
                                                <img src={"/images/left_chevron.png"} alt="LEFT" />
                                            </button>
                                        </div>
                                        <div className="control">
                                            <button
                                                className="button is-info is-large"
                                                disabled={this.state.playersTurn === false}
                                                onClick={this.selectCard}
                                            >
                                                <img src={"/images/dot_and_circle.png"} alt="SUBMIT" />
                                            </button>
                                        </div>
                                        <div className="control">
                                            <button
                                                className="button is-info is-large"
                                                disabled={this.state.playersTurn === false}
                                                onClick={() => this.submitDirection("right")}
                                            >
                                                <img src={"/images/right_chevron.png"} alt="RIGHT" />
                                            </button>
                                        </div>
                                    </div>
                                    <div className="field is-grouped is-grouped-centered">
                                        <div className="control">
                                            <button className="button is-large noButton" disabled></button>
                                        </div>
                                        <div className="control">
                                            <button 
                                                className="button is-info is-large"
                                                disabled={this.state.playersTurn === false}
                                                onClick={() => this.submitDirection("down")}
                                            >
                                                <img src={"/images/down_chevron.png"} alt="DOWN" />
                                            </button>
                                        </div>
                                        <div className="control">
                                            <button className="button is-large noButton" disabled></button>
                                        </div>
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

export default Match;