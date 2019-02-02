import React from 'react';

class Fragments extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            fragments: [],
            fragmentChosen: false
        }
    }

    componentDidMount() {
        this.props.socket.on('turn', (data) => {
            console.log(data);
            this.setState({
                fragments: data.fragments,
                fragmentChosen: false
            });
        });

        window.addEventListener('beforeunload', this.onPageRefresh);
    }

    onPageRefresh = () => {
        this.props.socket.emit('refresh');
    };

    selectPicture = (data) => {     
        // Only submit chosen image once per turn
        if (!this.state.fragmentChosen) {
            console.log(data);
            this.setState({ fragmentChosen: true }, () => {
                this.props.socket.emit('select', {
                    "player": this.props.userState.username,
                    "selection": data
                });    
            });
        }    
    }
    
    render() {
        return (
            <div className="hero is-fullheight">
                <div className="hero-body">
                    <div className="container has-text-centered">
                        <div className="columns is-1 is-variable is-mobile">
                            <div className="column">
                                <div className="level">
                                    <img
                                        className="image"
                                        src={`/images/fragments/${this.state.fragments[0]}`}
                                        alt="Fragment 1"
                                        onClick={() => this.selectPicture(this.state.fragments[0])}
                                    />
                                </div>
                                <div className="level">
                                    <img
                                        className="image"
                                        src={`/images/fragments/${this.state.fragments[3]}`}
                                        alt="Fragment 4"
                                        onClick={() => this.selectPicture(this.state.fragments[3])}
                                    />
                                </div>
                                <div className="level">
                                    <img
                                        className="image"
                                        src={`/images/fragments/${this.state.fragments[6]}`}
                                        alt="Fragment 7"
                                        onClick={() => this.selectPicture(this.state.fragments[6])}
                                    />
                                </div> 
                            </div>
                            <div className="column">
                                <div className="level">
                                    <img
                                        className="image"
                                        src={`/images/fragments/${this.state.fragments[1]}`}
                                        alt="Fragment 2"
                                        onClick={() => this.selectPicture(this.state.fragments[1])}
                                    />
                                </div>
                                <div className="level">
                                    <img
                                        className="image"
                                        src={`/images/fragments/${this.state.fragments[4]}`}
                                        alt="Fragment 5"
                                        onClick={() => this.selectPicture(this.state.fragments[4])}
                                    />
                                </div>
                                <div className="level">
                                    <img
                                        className="image"
                                        src={`/images/fragments/${this.state.fragments[7]}`}
                                        alt="Fragment 8"
                                        onClick={() => this.selectPicture(this.state.fragments[7])}
                                    />
                                </div>
                            </div>
                            <div className="column">
                                <div className="level">
                                    <img
                                        className="image"
                                        src={`/images/fragments/${this.state.fragments[2]}`}
                                        alt="Fragment 3"
                                        onClick={() => this.selectPicture(this.state.fragments[2])}
                                    />
                                </div>
                                <div className="level">
                                    <img
                                        className="image"
                                        src={`/images/fragments/${this.state.fragments[5]}`}
                                        alt="Fragment 6"
                                        onClick={() => this.selectPicture(this.state.fragments[5])}
                                    />
                                </div>
                                <div className="level">
                                    <img
                                        className="image"
                                        src={`/images/fragments/${this.state.fragments[8]}`}
                                        alt="Fragment 9"
                                        onClick={() => this.selectPicture(this.state.fragments[8])}
                                    />
                                </div>   
                            </div>
                        </div>
                    </div>
                    <div className={this.state.fragmentChosen ? "modal is-active" : "modal"}>
                        <div className="modal-background"></div>
                        <div className="modal-content">
                            <div className="columns is-centered has-text-centered">
                                <div className="column">
                                    <h5 className="title is-5 has-text-white">Fragment Chosen</h5>    
                                </div>
                            </div>  
                        </div>
                    </div>
                </div>  
            </div>
        );
    }
}

export default Fragments;