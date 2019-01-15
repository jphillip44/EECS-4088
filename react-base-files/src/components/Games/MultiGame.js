import React from 'react';

class MultiGame extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            name: '',
            valid: '',
            tapCount: 0,
            simonSequence: [],
            mathAnswer: 0,
            activateButton: 0
        }
    }
    
    componentDidMount() {
        this.props.socket.on('state', (data) => {
            this.setState({
                name: data.name,
                valid: data.valid,
                tapCount: 0,
                simonSequence: [],
                mathAnswer: 0
            });
            console.log(data);
        });
        this.props.socket.on('timerExpired', (data) => {
            console.log('timerExpired');
            let answer;
            if (this.state.name === "MultiTap") {
                answer = this.state.tapCount;
            } else if (this.state.name === "QuickMaff") {
                answer = this.state.mathAnswer;
            } else {
                answer = this.state.simonSequence
            }
            this.props.socket.on('action', answer);
        });
    }

    componentWillUnmount() {
        this.props.socket.removeAllListeners();
    }

    lightSequence = () => {
        // For activateButton: 1 = green, 2 = red, 3 = yellow, 4 = blue
        this.interval = setInterval(() => {

        }, 500);
    }

    submitTap = () => {
        this.setState({ tapCount: this.state.tapCount + 1 });
    }
    
    render() {
        return (
            <div className="hero is-fullheight">
                <div className="hero-body">
                    <div className="container has-text-centered">
                        <div className="column is-5">
                            <div className={this.state.name === "Simon" ? "box" : "box is-hidden"}>
                                <p>Simon</p>
                                <div className="buttons">
                                    <button className="button is-large is-success">G</button>
                                    <button className="button is-large is-danger">R</button>
                                </div>
                                <div className="buttons">
                                    <button className="button is-large is-warning">Y</button>
                                    <button className="button is-large is-info">B</button>
                                </div>
                            </div>
                            <div className={this.state.name === "MultiTap" ? "box" : "box is-hidden"}>
                                <p>MultiTap</p>
                                <p>Tap {this.state.valid} times</p>
                                <button
                                    className="button is-large is-primary"
                                    onClick={this.submitTap}
                                >
                                    TAP
                                </button>
                            </div>
                            <div className={this.state.name === "QuickMaff" ? "box" : "box is-hidden"}>
                                <p>QuickMaff</p>      
                                <div className="field">
                                    <span>{this.state.valid}</span> 
                                    <div className="control">
                                        <input
                                            className="input"
                                            type="text"
                                            placeholder="Enter answer"
                                        />
                                    </div>                                 
                                </div>  
                                <div className="field">
                                    <div className="control">
                                        <button className="button is-primary is-fullwidth">Enter</button>
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

export default MultiGame;