import React from 'react';

class Match extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            direction: '',
            flip: false,
            playersTurn: true
        };
    }

    componentDidMount() {
        this.props.socket.on('turn', (data) => {
            console.log(data.players);
        });

        this.props.socket.on('flip', (data) => {
            console.log(data);
            this.setState({ flip: true });
        });

        this.props.socket.on('timeout', (data) => {
            console.log(data);
            this.setState({ playersTurn: false });
        });


    }

    submitDirection = (direction) => {
        this.setState({ direction: direction }, () => {
            this.props.socket.emit(`${this.state.direction}`);
            console.log(`${this.state.direction}`);    
        });      
    }

    selectCard = () => {
        this.props.socket.emit('select');
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
                                    <img
                                        className="image"
                                        src={this.state.flip === true ? "/images/explosion.png" : "/images/explosion.png"}
                                        alt="Card"
                                    />
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
                                                onClick={this.submitDirection}
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