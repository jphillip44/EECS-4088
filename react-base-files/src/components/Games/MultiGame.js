import React from 'react';

class MultiGame extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            name: '',
            valid: '',
            playerHealth: '',
            tapCount: 0,
            simonSequence: [],
            mathAnswer: 0,
            activateButton: 0
        }
    }

    componentDidMount() {
        this.props.socket.on('state', (data) => {
            let user = this.props.userState.username;
            this.setState({
                name: data.name,
                valid: data.valid,
                playerHealth: data.players[user].hp,
                tapCount: 0,
                simonSequence: [],
                mathAnswer: 0
            });
            console.log(data);
            console.log("Player Health: " + this.state.playerHealth);
        });
        // Submit relevant data of the current game to the server on expiration of timer
        this.props.socket.on('timerExpired', (data) => {
            console.log('timerExpired');
            let answer;
            if (this.state.name === "MultiTap") {
                answer = this.state.tapCount;
            } else if (this.state.name === "QuickMaff") {
                answer = this.state.mathAnswer;
                console.log(answer);
            } else {
                answer = this.state.simonSequence
            }
            this.props.socket.emit('action', {
                player: this.props.userState.username,
                valid: answer 
            });
        });
        
        // Custom text is not allowed, so the string below is just used to get 
        // the pop up warning
        window.addEventListener('beforeunload', (event) => {
            event.returnValue = "Refreshing the page will break things";
        });
    }

    componentWillUnmount() {
        this.props.socket.removeAllListeners();
    }
    // Counts the number of taps in Tap Counter
    submitTap = () => {
        this.setState({ tapCount: this.state.tapCount + 1 });
    }
    // Record order of colour selection in Simon Says
    submitSimon = (data) => {
        let temp = [];
        temp = this.state.simonSequence;
        temp.push(data);
        this.setState({ simonSequence: temp });
    }
    // Logic behind digit display in QuickMaff
    submitMaff = (data) => {
        if (data === "delete") {
            this.setState({ mathAnswer: Math.trunc(this.state.mathAnswer / 10) });       
        } else if (data === "minus") {
            this.setState({ mathAnswer: this.state.mathAnswer * -1 });
        } else {
            this.setState({ mathAnswer: this.state.mathAnswer * 10 + data });
        }
    }
    
    render() {
        return (
            <div className="hero is-fullheight">
                <div className="hero-body">
                    <div className="container has-text-centered">
                        <div className="columns is-centered">
                            <div className="column is-5">
                                <div className={this.state.name === "Simon" ? "box" : "box is-hidden"}>
                                    <div className="columns is-1 is-variable is-mobile">
                                        <div className="column">
                                            <div className="buttons">
                                                <span className="button is-fullwidth is-large is-success" onClick={() => this.submitSimon("Green")}>G</span>
                                                <span className="button is-fullwidth is-large is-danger" onClick={() => this.submitSimon("Red")}>R</span>
                                            </div>
                                        </div>
                                        <div className="column">
                                            <div className="buttons">
                                                <span className="button is-fullwidth is-large is-warning" onClick={() => this.submitSimon("Yellow")}>Y</span>
                                                <span className="button is-fullwidth is-large is-info" onClick={() => this.submitSimon("Blue")}>B</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div
                                    className={this.state.name === "MultiTap" ? "box multiTap" : "box is-hidden"}
                                    onClick={this.submitTap}
                                >
                                    <h5 className="title is-5">Tap Here</h5>
                                </div>
                                <div className={this.state.name === "QuickMaff" ? "box" : "box is-hidden"}>
                                    <h4 className="title is-4">QuickMaff</h4>     
                                    <div className="field">
                                        <div className="control">
                                            <input
                                                className="input is-medium"
                                                type="text"
                                                value={this.state.mathAnswer}
                                                readOnly
                                            />
                                        </div>                                 
                                    </div>
                                    <div className="columns is-1 is-variable is-mobile">
                                        <div className="column">
                                            <div className="buttons">
                                                <span className="button is-fullwidth is-large is-info" onClick={() => this.submitMaff(1)}>1</span>
                                                <span className="button is-fullwidth is-large is-info" onClick={() => this.submitMaff(4)}>4</span>
                                                <span className="button is-fullwidth is-large is-info" onClick={() => this.submitMaff(7)}>7</span>
                                                <span className="button is-fullwidth is-large is-info" onClick={() => this.submitMaff("minus")}>-</span>
                                            </div>     
                                        </div>
                                        <div className="column">
                                            <div className="buttons">
                                                <span className="button is-fullwidth is-large is-info" onClick={() => this.submitMaff(2)}>2</span>
                                                <span className="button is-fullwidth is-large is-info" onClick={() => this.submitMaff(5)}>5</span>
                                                <span className="button is-fullwidth is-large is-info" onClick={() => this.submitMaff(8)}>8</span>
                                                <span className="button is-fullwidth is-large is-info" onClick={() => this.submitMaff(0)}>0</span>
                                            </div>                          
                                        </div>
                                        <div className="column">
                                            <div className="buttons">
                                                <span className="button is-fullwidth is-large is-info" onClick={() => this.submitMaff(3)}>3</span>
                                                <span className="button is-fullwidth is-large is-info" onClick={() => this.submitMaff(6)}>6</span>
                                                <span className="button is-fullwidth is-large is-info" onClick={() => this.submitMaff(9)}>9</span>
                                                <span className="button is-fullwidth is-large is-info" onClick={() => this.submitMaff("delete")}>
                                                    <img src="/images/multigame/reply.png" alt="Delete" />
                                                </span>
                                            </div>    
                                        </div>
                                    </div>                                                                
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className={this.state.playerHealth === "dead" ? "modal is-active" : "modal"}>
                        <div className="modal-background"></div>
                        <div className="modal-content">
                            <div className="box has-text-centered">
                                <h5 className="title is-5">You Are Dead</h5>
                            </div>     
                        </div>
                    </div>
                </div>  
            </div>
        );
    }
}

export default MultiGame;