import React from 'react';

class Match extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            flip: false,
            playersTurn: false,
            cursor: [],
            board: [],
            unselectableCards: [],
            cardSelected: false,
            cardValue: '',
            disableSubmit: false
        };
    }

    componentDidMount() {
        this.props.socket.on('turn', (data) => {
            // if next in state is the clients username
            if (data.next[0] === this.props.userState.username) {
                this.setState({
                    playersTurn: true,
                    cursor: data.cursor,
                    board: data.board
                });
            } else {
                this.setState({ playersTurn: false });
            }
            // get matched cards and selected card location from gameboard
            let i, j;
            let temp = [];
            for (i = 0; i < data.gameBoard.length; i++) {
                for (j = 0; j < data.gameBoard[0].length; j++) {
                    if (!(data.gameBoard[i][j] === "XX")) {
                        temp.push([i, j]);
                    }
                }
            }
            this.setState({ unselectableCards: temp }, () => {
                console.log(this.state.unselectableCards);
                this.findUnselectable(data.cursor);
            });           
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
            this.findUnselectable(data);
            // If there is no match, than put cursor location into state
            this.setState({ cursor: data });
            console.log(data);
        });

        this.props.socket.on('timeout', (data) => {
            console.log('timeout');
        });

        window.addEventListener('beforeunload', this.onPageRefresh);
    }

    componentWillUnmount() {
        this.props.socket.removeAllListeners();
    }

    onPageRefresh = () => {
        this.props.socket.emit('refresh');
    };

    findUnselectable = (data) => {
        // compare cursor location to unselectableCards location list and disable
        // submit button if there is a match
        let i;
        for (i = 0; i < this.state.unselectableCards.length; i++) {
            if (this.state.unselectableCards[i][0] === data[0] && this.state.unselectableCards[i][1] === data[1]) {
                this.setState({
                    disableSubmit: true,
                    cursor: data
                }); 
            }
        }
    }

    submitDirection = (direction) => {
        // Reset disableSubmit to default of false
        this.setState({ disableSubmit: false }, () => {
            // Emit cursor direction to server when a directional button is clicked
            this.props.socket.emit(direction);      
        });          
    }

    selectCard = () => {
        this.setState({
            cardValue: this.state.board[this.state.cursor[0]][this.state.cursor[1]],
            cardSelected: true
        });
        this.props.socket.emit('select');
    }

    flipCard = () => {       
        this.setState({ flip: false }, () => {
            clearInterval(this.interval);
            this.interval = setInterval(() => this.hideBox(), 1000);     
        });
    }

    hideBox = () => {
        clearInterval(this.interval);
        this.setState({ cardSelected: false });
    }
    
    render() {
        return (
            <div className="hero is-fullheight">
                <div className="hero-body">
                    <div className="container has-text-centered">
                        <div className="columns is-centered">
                            <div className="column is-4">
                                <div className={this.state.cardSelected === true ? "box" : "box is-hidden" }>
                                    <div className={this.state.flip === true ? "flip-container flip" : "flip-container"}>
                                        <div className="flipper">
                                            <div className="front">
                                                <img src={"/images/match/cards/card_back.png"} alt="Card Back" />
                                            </div>
                                            <div className="back">
                                                <img
                                                    src={`/images/match/cards/card_${this.state.cardValue}.png`}
                                                    alt={`Card ${this.state.cardValue}`}
                                                />
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div className={this.state.cardSelected === false ? "box" : "box is-hidden" }>
                                    <h2 className="title is-2">Select A Card</h2>
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
                                                <img src="/images/match/up_chevron.png" alt="UP" />
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
                                                <img src="/images/match/left_chevron.png" alt="LEFT" />
                                            </button>
                                        </div>
                                        <div className="control">
                                            <button
                                                className="button is-info is-large"
                                                disabled={this.state.playersTurn === false || this.state.disableSubmit === true}
                                                onClick={this.selectCard}
                                            >
                                                <img src="/images/match/dot_and_circle.png" alt="SUBMIT" />
                                            </button>
                                        </div>
                                        <div className="control">
                                            <button
                                                className="button is-info is-large"
                                                disabled={this.state.playersTurn === false}
                                                onClick={() => this.submitDirection("right")}
                                            >
                                                <img src="/images/match/right_chevron.png" alt="RIGHT" />
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
                                                <img src="/images/match/down_chevron.png" alt="DOWN" />
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